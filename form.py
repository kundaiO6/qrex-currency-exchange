from flet import *
import json
import requests

with open("./assets/country-phone-codes-locale-currency.json") as f:
    data = json.load(f)

def submit(e):
    payload = {
        "phone_number": phone_number.value,
        "country": country.value, 
        "currency": currency.value, 
        "action": Action.value, 
        "at": At.value, 
        "pair": pair.value}
    r=requests.post('http://127.0.0.1:8000/native/', data=payload)
    print(f"{phone_number.value, country.value, currency.value, Action.value, At.value, pair.value}")
    print(f"result {r}")
phone_number = TextField(label=f"Phone No.", width=200, height=40)

country = Dropdown(
                label="country",
                width=200,
                height=40
            )
for x in data:
    country.options.append( dropdown.Option(data[x]['name']))

Action =  Dropdown( 
                label="Action",
                width=100,
                height=40,
                options=[
                    dropdown.Option("Buying"),
                    dropdown.Option("Selling")
                ]
            )

At = TextField(label="At (exchange rate)", width=100, height=40)
currency = Dropdown(
                label="currency",
                width=100, height=40
            )
for x in data:
   if 'currency' in data[x]:
      currency.options.append( dropdown.Option(data[x]['currency']))
else:
    pass

pair = Dropdown(
                label="to",
                width=200, 
                height=40
            )
for x in data:
   if 'currency' in data[x]:
      pair.options.append( dropdown.Option(data[x]['currency']))
else:
    pass

Form = Container(
    content=Column(
        controls=[
            Container( content=Text("Let`s make a listing")),
            phone_number,
             country,
            Action,
            Row([currency, At], alignment="wrap"),
            pair,
            Container(content=TextButton(width=200, style=ButtonStyle( padding=padding.all(0),bgcolor="green", color="white"),text="Continue", content=Row([Text("Continue"), Icon(name=icons.ARROW_FORWARD_IOS, size=13)], alignment=MainAxisAlignment.CENTER), on_click=submit))
        ]
    )
)
