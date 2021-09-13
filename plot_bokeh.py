def _initialize(theme = 'dark_minimal',jupyter=True):
    
    if jupyter:
        from bokeh.io import output_notebook ,curdoc
        output_notebook()
    else:
        from bokeh.io import curdoc
    
    curdoc().theme = theme

def geo_circle(geodataframe ,title,w ,h ,hovertool=None, cmp_colum = None ,palette_name = None,
               alpha=None,circle_size=None,circle_color=None,cmp = False,ax =False,tile = True,
               cmp_scale = None,cmp_min=None,cmp_max=None,tile_name = 'dark'):

    if tile: 
        if tile_name =='dark':
            tile = {'url':'https://tiles.basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}@2x.png'}
        else:
            tile = {'url':'https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png'}
    else:
      tile ={}
    
    from bokeh.plotting import figure
    from bokeh.models import GeoJSONDataSource,ColumnDataSource,ColorBar,\
    BasicTicker,WMTSTileSource

    circles = GeoJSONDataSource(geojson=geodataframe.to_json())
    tile_options = WMTSTileSource(**tile)
    p = figure(title=title,plot_width=w, plot_height=h,tooltips=hovertool)
    p.add_tile(tile_options)
    p.axis.visible = ax
    
    if cmp:
        
        if cmp_min is None:
            cmp_min = geodataframe[cmp_colum].min()
        
        if cmp_max is None:
            cmp_max = geodataframe[cmp_colum].max()

        if cmp_scale == 'linear':
            from bokeh.models import LinearColorMapper
            color_mapper = LinearColorMapper(palette = palette_name , low = cmp_min,
                                             high = cmp_max)
        else:
            from bokeh.models import LogColorMapper
            color_mapper = LogColorMapper(palette = palette_name , low = cmp_min,
                                             high = cmp_max)
            
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),location=(0,0),
                                 label_standoff=15)
        p.add_layout(color_bar, 'left')
        p.circle(source=circles,size=circle_size, color={'field' :cmp_colum, 'transform': color_mapper}, alpha=alpha)
    else :
        p.circle(source=circles,size=circle_size, color=circle_color, alpha=alpha)

    return p


def geo_line(geodataframe ,title,w ,h ,hovertool=None, cmp_colum = None ,palette_name = None,
               line_alpha=None,line_width=None,line_color=None,cmp = False,ax =False,tile = True,
               cmp_scale = None,cmp_min=None,cmp_max=None,cmp_factors=None,categorical_palette=None):

    if tile: 
      tile = {'url':'https://tiles.basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}@2x.png'}
    else:
      tile ={}
    
    from bokeh.plotting import figure
    from bokeh.models import GeoJSONDataSource,ColumnDataSource,ColorBar,\
    BasicTicker,WMTSTileSource

    lines = GeoJSONDataSource(geojson=geodataframe.to_json())
    tile_options = WMTSTileSource(**tile)
    p = figure(title=title,plot_width=w, plot_height=h,tooltips=hovertool)
    p.add_tile(tile_options)
    p.axis.visible = ax
    
    if cmp:
        
        if cmp_min is None:
            cmp_min = geodataframe[cmp_colum].min()
        
        if cmp_max is None:
            cmp_max = geodataframe[cmp_colum].max()

        if cmp_scale == 'linear':
            from bokeh.models import LinearColorMapper
            color_mapper = LinearColorMapper(palette = palette_name , low = cmp_min,
                                             high = cmp_max)
            color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),location=(0,0),
                                 label_standoff=15)
            p.add_layout(color_bar, 'left')
            
        elif cmp_scale == 'categorical':
            from bokeh.models import CategoricalColorMapper
            color_mapper = CategoricalColorMapper(factors = cmp_factors,palette = categorical_palette )
            
        else:
            from bokeh.models import LogColorMapper
            color_mapper = LogColorMapper(palette = palette_name , low = cmp_min,
                                             high = cmp_max)
            color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),location=(0,0),
                                 label_standoff=15)
            p.add_layout(color_bar, 'left')
            
        p.multi_line(source=lines,line_width=line_width, line_color={'field' :cmp_colum, 'transform': color_mapper},\
                    alpha=line_alpha)
    else :
        p.multi_line(source=lines,line_width=line_width, line_color=line_color, line_alpha=line_alpha)

    return p


def geo_area(geodataframe ,title,w ,h ,hovertool=None, cmp_colum = None ,palette_name = None,
               area_alpha=None,area_color=None,cmp = False,ax =False,tile = True,
               cmp_scale = None,cmp_min=None,cmp_max=None,cmp_factors=None,categorical_palette=None):

    if tile: 
      tile = {'url':'https://tiles.basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}@2x.png'}
    else:
      tile ={}
    
    from bokeh.plotting import figure
    from bokeh.models import GeoJSONDataSource,ColumnDataSource,ColorBar,\
    BasicTicker,WMTSTileSource

    area = GeoJSONDataSource(geojson=geodataframe.to_json())
    tile_options = WMTSTileSource(**tile)
    p = figure(title=title,plot_width=w, plot_height=h,tooltips=hovertool)
    p.add_tile(tile_options)
    p.axis.visible = ax
    
    if cmp:
        
        if cmp_min is None:
            cmp_min = geodataframe[cmp_colum].min()
        
        if cmp_max is None:
            cmp_max = geodataframe[cmp_colum].max()

        if cmp_scale == 'linear':
            from bokeh.models import LinearColorMapper
            color_mapper = LinearColorMapper(palette = palette_name , low = cmp_min,
                                             high = cmp_max)
            color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),location=(0,0),
                                 label_standoff=15)
            p.add_layout(color_bar, 'left')
            
        elif cmp_scale == 'categorical':
            from bokeh.models import CategoricalColorMapper
            color_mapper = CategoricalColorMapper(factors = cmp_factors,palette = categorical_palette )
            
        else:
            from bokeh.models import LogColorMapper
            color_mapper = LogColorMapper(palette = palette_name , low = cmp_min,
                                             high = cmp_max)
            color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),location=(0,0),
                                 label_standoff=15)
            p.add_layout(color_bar, 'left')
            
        p.patches('xs','ys', source=area, fill_alpha=area_alpha, line_width=0.5, line_color='black',
            fill_color={'field' :cmp_colum, 'transform': color_mapper})
    else :
        p.patches('xs','ys', source=area, fill_alpha=area_alpha, line_width=0.5, line_color='black',color=area_color)        

    return p