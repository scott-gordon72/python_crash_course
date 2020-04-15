def make_car(mfg, model, **car_info):
    """Build a dictionary for a car"""
    car_info['mfg'] = mfg
    car_info['model'] = model

    return car_info

# Create two cars with different kinds of info.
car_0 = make_car('ford', 'taurus', engine='v6', mpg=32, year=2008)
car_1 = make_car('chevy', 'topaz', engine='v6', mpg=28, year=1992)
car_2 = make_car('lexus', 's400', engine='v8', mpg=24, year=1999)

print(car_0)
print(car_1)
print(car_2)
