async def ranks(message, client):
    string = "```These are the ranks: \n" \
             "-Pirate Lord (Admins) \n"\
                "-Captains\n"\
                "-First Mate\n"\
                "-QuarterMaster\n"\
                "-Buccaneers\n"\
                "-Crew Member```"
    await client.send_message(message.channel, string)
