import jinja2



def display_page(image):

    outputfile = 'myfile.html'

    subs = jinja2.Environment(loader = jinja2.FileSystemLoader('./')).get_template('template.html').render(mydata=image)
    
    with open(outputfile,'w') as f:
        f.write(subs)