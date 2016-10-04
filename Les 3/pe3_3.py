def lang_genoeg(lengte):
    if lengte >= 120:
        return "Je bent lang genoeg voor de atractie!"
    else:
        return "Sorry, je bent te klein!"
lengte = eval(input("Wat is uw lengte ?"))
print(lang_genoeg(lengte))
