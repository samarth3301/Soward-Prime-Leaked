import re

from discord.ext import commands

# Time Variables
time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"s": 1, "m": 60, "h": 3600, "d": 86400}


class TimeConverter(commands.Converter):
    """TimeConverter Class

    Attributes:
      - convert: The converter itself.
    """

    async def convert(self, ctx, argument):
        """Converts the value i.e. "1h 32m" to secs.

        Args:
            ctx (commands.Context): The command context.
            argument (argument): The value to convert to seconds.

        Raises:
            commands.BadArgument: The value is invalid, (s|m|h|d) are valid keys.
            commands.BadArgument: The key is not a number.

        Returns:
            seconds: No. of seconds.
        """
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(
                    f"{value} is an invalid time key! s|m|h|d are valid arguments"
                )
            except ValueError:
                raise commands.BadArgument(f"{key} is not a number!")
        return round(time)


class TimeHumanizer:
    """Converts seconds to human-readable format.
    Args:
        value (int): The value to convert
    Raises:
        commands.BadArgument: If time is negative.
    """

    def __new__(self, value: int):
        if value <= 0:
            raise commands.BadArgument("Time cannot be negative.")

        duration = ""

        minutes, seconds = divmod(value, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)

        duration += f"{months} months, " if months > 0 else ""
        duration += f"{days} days, " if days > 0 else ""
        duration += f"{hours} hours, " if hours > 0 else ""
        duration += f"{minutes} minutes, " if minutes > 0 else ""
        duration += f"{seconds} seconds" if seconds > 0 else ""
        duration = duration.strip(", ")
        if months == 1:
            duration = duration.replace("months", "month")
        if days == 1:
            duration = duration.replace("days", "day")
        if hours == 1:
            duration = duration.replace("hours", "hour")
        if minutes == 1:
            duration = duration.replace("minutes", "minute")
        if seconds == 1:
            duration = duration.replace("seconds", "second")

        return duration
