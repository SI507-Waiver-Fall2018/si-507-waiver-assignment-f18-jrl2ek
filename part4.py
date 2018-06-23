# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
import csv

def main():
    #offline.init_notebook_mode()
    py.sign_in('jrlint', 'tSc9W7gbINGUvDxgAgTS')
    with open('noun_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        nouns = []
        nums = []
        for row in reader:
            print(row['Noun'], row['Number'])
            nouns.append(row['Noun'])
            nums.append(row['Number'])
        data = [go.Bar(x=nouns, y=nums)]
        layout = go.Layout(title='Most Common Nouns', width=800, height=800)
        fig = go.Figure(data=data, layout=layout)
        #offline.plot(data:data1, layout: layout1)
        py.image.save_as(fig, filename='part_viz_image.png')


if __name__ == "__main__":
    main()



# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
