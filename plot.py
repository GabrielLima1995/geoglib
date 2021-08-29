def geo_bokeh_circle(geodataframe,range_x,range_y,tile,theme_bokeh,
                          graph_title,size_circle=None,fill_c=None,line_c=None,fill_a=None,output_name=None,cmp =False,
                          axis=False,pallete_name= None,axis_type=None,column_color=None):
    import geopandas as gpd
    from bokeh.plotting import figure, output_file, show
    from bokeh.tile_providers import get_provider
    from bokeh.themes import built_in_themes
    from bokeh.io import output_notebook ,curdoc
    from bokeh.models import ColumnDataSource,ColorBar,BasicTicker
    from bokeh.models import LinearColorMapper
    output_notebook()
    
    tile_provider = get_provider(tile)
    curdoc().theme = theme_bokeh
    
    p = figure(x_range= range_x,y_range= range_y,x_axis_type=axis_type, y_axis_type=axis_type,title=graph_title)
    p.add_tile(tile_provider)

    
    if cmp:
        source = ColumnDataSource(
        data = dict(
		latitude = geodataframe.geometry.y.tolist(),
		longitude = geodataframe.geometry.x.tolist(),
		color = column_color.tolist()))
        cmap = LinearColorMapper(palette= pallete_name,low = column_color.min(),high = column_color.max())

        p.circle(x='longitude', y='latitude',color = {'field':'color','transform':cmap},source = source )
        color_bar = ColorBar(color_mapper=cmap, ticker=BasicTicker(),location=(0,0))
        p.add_layout(color_bar, "left")
        
    else :
        
        p.circle(x=geodataframe.geometry.x, y=geodataframe.geometry.y,size=size_circle,fill_color=fill_c, line_color=line_c,fill_alpha=fill_a)
    
    p.axis.visible = axis
    output_file(output_name)
    show(p)
