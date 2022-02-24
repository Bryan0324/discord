import requests
r = requests.get("https://blox-fruits.fandom.com/wiki/Codes").text.split("</tbody>")[1]
print(r)
print("wryy")
w = 1
a = 0
#r.split("<td><b>")[1].split("</b>")[0]
while w == 1:
    try:
        print(r.split("<td><b>")[a+1].split("</b>")[0])
        print(r.split("<td><b>")[a+1].split("</b>")[1].split("<td>")[1].split("</td></tr>")[0])
        print()
        a = a + 1
    except:
        w = 0

