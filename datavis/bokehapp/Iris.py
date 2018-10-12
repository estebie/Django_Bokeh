from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource
from bokeh.embed import components
from bokeh.resources import CDN

colormap={'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
urlmap = {
            'setosa':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
            'versicolor':'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg',
            'virginica':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg'
         }
flowers['imgs']=[urlmap[x] for x in flowers['species']]
flowers['color']=[colormap[x] for x in flowers['species']]
flowers['size']=[(size * 4) for size in flowers['sepal_width']]

setosa=ColumnDataSource(flowers[flowers["species"]=="setosa"])
versicolor=ColumnDataSource(flowers[flowers["species"]=="versicolor"])
virginica=ColumnDataSource(flowers[flowers["species"]=="virginica"])

cds_dict = {'setosa':setosa, 'versicolor':versicolor, 'virginica':virginica}
#Define the output file path
output_file("iris.html")

#Create the figure object
f=figure()

#print(cds_dict['setosa'])
#adding glyphs
for specie in flowers['species'].unique():
#     print(cds_dict[specie])
    f.circle(
            x="petal_length",
            y="petal_width",
            size="size",
            fill_alpha=0.2,
            color="color",
            line_dash=[5,3],
            legend=specie.capitalize(),
            source=cds_dict[specie]
            )


#Style the tools
f.tools=[PanTool(), ResetTool()]
# hover=HoverTool(tooltips=[("Species", "@species"), ("Sepal Width", "@sepal_width")])
hover=HoverTool(tooltips="""
    <div>
        <div>
            <img
                src="@imgs" height="42" alt="@imgs" width=42
                style="float: left; margin: 0px 15px 15px 0px;"
            ></img>
        </div>
        <div>
            <span style="font-size: 13px; color: #966;">$index</span>
            <span style="font-size: 15px; font-weight: bold;">@species</span>
        </div>
        <div>
            <span style="font-size: 10px; color: #696;">Petal length: @petal_length</span><br>
            <span style="font-size: 10px; color: #696;">Petal width: @petal_width</span>
        </div>
    </div>
""")
f.add_tools(hover)
f.toolbar_location='above'
f.toolbar.logo=None

#Style the legend
f.legend.location = "top_left"
f.legend.background_fill_alpha = 0
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 18
f.legend.spacing = 1
f.legend.label_text_color = 'olive'
f.legend.label_text_font = 'antiqua'

#show(f)
js,div=components(f)

cdn_js=CDN.js_files[0]
cdn_css=CDN.css_files[0]