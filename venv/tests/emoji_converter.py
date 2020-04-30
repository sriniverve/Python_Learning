'''
This is programs to create shortcuts for emojis
'''

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "☹"
}
output = ""
for word in words:
    output += emojis.get(word, word)+' '

print(output)
