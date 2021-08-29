def _initialize(theme = 'dark_minimal',jupyter=True):
    
    if jupyter:
        from bokeh.io import output_notebook ,curdoc
        output_notebook()
    else:
        from bokeh.io import curdoc
    
    curdoc().theme = theme

def geo_circle(geodataframe ,title,w ,h ,hovertool=None, cmp_colum = None ,palette_name = None,
               alpha=None,circle_size=None,circle_color=None,cmp = False,ax =False,tile = True):

    if tile: 
      tile = {'url':'https://tiles.basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}@2x.png'}
    else:
      tile ={}
    
    from bokeh.plotting import figure
    from bokeh.models import GeoJSONDataSource,ColumnDataSource,ColorBar,\
    BasicTicker,LinearColorMapper,WMTSTileSource

    circles = GeoJSONDataSource(geojson=geodataframe.to_json())
    tile_options = WMTSTileSource(**tile)
    p = figure(title=title,plot_width=w, plot_height=h,tooltips=hovertool)
    p.add_tile(tile_options)
    p.axis.visible = ax
    
    if cmp:
        color_mapper = LinearColorMapper(palette = palette_name , low = geodataframe[cmp_colum].min(),
                                 high = geodataframe[cmp_colum].max())
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),location=(0,0),
                                 label_standoff=15)
        p.add_layout(color_bar, 'left')
        p.circle(source=circles,size=circle_size, color={'field' :cmp_colum, 'transform': color_mapper}, alpha=alpha)
    else :
        p.circle(source=circles,size=circle_size, color=circle_color, alpha=alpha)

    return p
