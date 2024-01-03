import logging
import collections

"""
A helper file for using mongo db
Class document aims to make using mongo calls easy, saves
needing to know the syntax for it. Just pass in the db instance
on init and the document to create an instance on and boom.

Made by: Skelmis | Edited by: MrNatural (For customisation purposes)
"""


class Document:
    def __init__(self, connection, document_name):
        """
        Our init function, sets up the conenction to the specified document

        Params:
         - connection (Mongo Connection) : Our database connection
         - documentName (str) : The document this instance should be
        """
        self.db = connection[document_name]
        self.logger = logging.getLogger(__name__)

    # <-- Pointer Methods -->
    async def get(self, id):
        """
        This is essentially find so point to that
        """
        return await self.find(id)

    async def get_if(self, dict):
        """
        For simpler calls, points to self.find_if
        """
        return await self.find_if(dict)

    # <-- Actual Methods -->
    async def find(self, id):
        """
        Returns the data found under `id`

        Params:
         -  id () : The id to search for

        Returns:
         - None if nothing is found
         - If somethings found, return that
        """
        return await self.db.find_one({"_id": id})

    async def find_if(self, dict):
        """
        Returns the data if value for the given key is same to provided value

        Params:
         - dict () : The dictionary with key, value to match and return data

        Returns:
         - None if nothing is found
         - If something found, return that
        """
        # Check if its actually a Dictionary
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary.")

        return await self.db.find_one(dict)

    async def delete(self, id):
        """
        Deletes all items found with _id: `id`

        Params:
         -  id () : The id to search for and delete
        """
        if not await self.find(id):
            return

        await self.db.delete_many({"_id": id})

    async def delete_if(self, dict):
        """
        Deletes all items found with _id: `id`

        Params:
         -  dict () : The dictionary with key, value to match
        """
        if not await self.find_if(dict):
            return

        await self.db.delete_many(dict)

    async def insert(self, dict):
        """
        insert something into the db

        Params:
        - dict (Dictionary) : The Dictionary to insert
        """
        # Check if its actually a Dictionary
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary.")

        # Always use your own _id
        if not dict["_id"]:
            raise KeyError("_id not found in supplied dict.")

        await self.db.insert_one(dict)

    async def upsert(self, dict):
        """
        Makes a new item in the document, if it already exists
        it will update that item instead

        This function parses an input Dictionary to get
        the relevant information needed to insert.
        Supports inserting when the document already exists

        Params:
         - dict (Dictionary) : The dict to insert
        """
        if await self.__get_raw(dict["_id"]) != None:
            await self.update(dict)
        else:
            await self.db.insert_one(dict)

    async def update(self, dict):
        """
        For when a document already exists in the data
        and you want to update something in it

        This function parses an input Dictionary to get
        the relevant information needed to update.

        Params:
         - dict (Dictionary) : The dict to insert
        """
        # Check if its actually a Dictionary
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary.")

        # Always use your own _id
        if not dict["_id"]:
            raise KeyError("_id not found in supplied dict.")

        if not await self.find(dict["_id"]):
            return

        id = dict["_id"]
        dict.pop("_id")
        await self.db.update_one({"_id": id}, {"$set": dict})

    async def unset(self, dict):
        """
        For when you want to remove a field from
        a pre-existing document in the collection

        This function parses an input Dictionary to get
        the relevant information needed to unset.

        Params:
         - dict (Dictionary) : Dictionary to parse for info
        """
        # Check if its actually a Dictionary
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary.")

        # Always use your own _id
        if not dict["_id"]:
            raise KeyError("_id not found in supplied dict.")

        if not await self.find(dict["_id"]):
            return

        id = dict["_id"]
        dict.pop("_id")
        await self.db.update_one({"_id": id}, {"$unset": dict})

    async def increment(self, id, amount, field):
        """
        Increment a given `field` by `amount`

        Params:
        - id () : The id to search for
        - amount () : Amount to increment by
        - field () : field to increment
        """
        if not await self.find(id):
            return

        await self.db.update_one({"_id": id}, {"$inc": {field: amount}})

    async def change(self, id, key, value):  # Idk if it works
        """
        Change a given `key` by `value`

        Params:
        - id () : The id to search for
        - key () : The key of the item to change
        - value () : The key's value
        """
        if not await self.find(id):
            return

        await self.db.update_one({"_id": id}, {"$inc": {key: value}})

    async def get_all(self):
        """
        Returns a list of all data in the document
        """
        data = []
        async for document in self.db.find({}):
            data.append(document)
        return data

    # <-- Private methods -->
    async def __get_raw(self, id):
        """
        An internal private method used to eval certain checks
        within other methods which require the actual data
        """
        return await self.db.find_one({"_id": id})


Database = Document
