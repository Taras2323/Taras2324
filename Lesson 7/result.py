result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ValueError:
        print("Помилка: a менше b")
    except IndexError:
        print("Помилка: b більше 100")
    except Exception as e:
        print("Інша помилка:", str(e))

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)