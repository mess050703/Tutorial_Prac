import matplotlib.pyplot as plt

catagories = ['Freshmen', 'Sophomores', 'Juniors', 'Seniors']
values = [300, 250, 275, 225]
colors = ['red', 'yellow', 'blue', 'green']

plt.pie (values, labels = catagories,
                 autopct= '%1.1f%%',
                 colors = colors,
                 explode = [0, 0, 0, 0.1],
                 shadow = True,
                 startangle = 90)

plt.title ('Bro Code College')

plt.show ()