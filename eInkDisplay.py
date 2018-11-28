import codecs


# Open SVG to process
output = codecs.open('weather-script-preprocess.svg', 'r', encoding='utf-8').read()
print("Processing SVG...")
#
# # Insert icons and temperatures
# output = output.replace('ICON_ONE',icons[0]).replace('ICON_TWO',icons[1]).replace('ICON_THREE',icons[2]).replace('ICON_FOUR',icons[3])
# output = output.replace('HIGH_ONE',str(highs[0])).replace('HIGH_TWO',str(highs[1])).replace('HIGH_THREE',str(highs[2])).replace('HIGH_FOUR',str(highs[3]))
# output = output.replace('LOW_ONE',str(lows[0])).replace('LOW_TWO',str(lows[1])).replace('LOW_THREE',str(lows[2])).replace('LOW_FOUR',str(lows[3]))
# print("...")
#
# #Insert book info
# output = output.replace('current_title',currentBook[0]).replace('reading_count',bookCount[0].strip())
# output = output.replace('#LINK_ONE',scriptDir + "\cover.jpg").replace('#LINK_TWO',scriptDir + "\NYcover.jpg")
#
# # Insert days of week
# day_string = str(day_one)
# one_day = datetime.timedelta(days=1)
# days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# output = output.replace('Today:',days_of_week[(day_one).weekday()]+' '+day_string[:10]).replace('DAY_THREE',days_of_week[(day_one + 2*one_day).weekday()]).replace('DAY_FOUR',days_of_week[(day_one + 3*one_day).weekday()])
# print("...")
#
# output = output.replace('agenda1_date',event_time[0]).replace('agenda1_title',event_title[0]).replace('agenda2_date',event_time[1]).replace('agenda2_title',event_title[1]).replace('agenda3_date',event_time[2]).replace('agenda3_title',event_title[2])
# print("...")

output = output.replace('Today:', 'dofjvbeklwdfndjvbelwdnbvhnfwjlfnj')

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)
print("Process complete.")