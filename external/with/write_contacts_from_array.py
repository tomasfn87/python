add_these = [
    {
        "name": "Pamela",
        "tel": "5211-0883"
    },
    {
        "name": "Patricia",
        "tel": "5284-4287"
    }
]

with open("contacts_sample.txt", "a") as fh:
    for i in add_these:
        fh.write(f'{i["name"]}, {i["tel"]}\n')
