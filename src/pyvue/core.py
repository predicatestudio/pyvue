"Core should hold the center of your app. This can then be referenced cli.py"
import re
from jinja2 import Environment, PackageLoader, select_autoescape
from pathlib import Path

env = Environment(
    loader=PackageLoader("pyvue", "templates"),
    # autoescape=select_autoescape()
)
template=env.get_template("base.html")

def get_tag(tag, text):
    match = re.search(f"(<{tag}()>)((.|\\n)*?)(<\/{tag}>)", text)
    return match[0]

class Vue():
    """Vue instances are representations of .vue files in python."""
    def __init__(self, filepath) -> None:
        self.fp = Path(filepath)
        with self.fp.open('r') as f:
            self.text = f.read()
            self.html_attrs = {}
            self.html_attrs["template"], self.template = self._read_tag("template")
            self.html_attrs["script"], self.script = self._read_tag("script")
            self.html_attrs["style"], self.style = self._read_tag("style")


    def _read_tag(self, tag):
        match = re.search(fr"(<{tag})((.|\n)*?)(<\/{tag}>)", self.text)
        if not match:
            return (None, None)
        html_attrs = self._get_html_attrs(match)
        tag_content = re.search(fr"(?<=>)((.|\n)*?)(?=<\/{tag}>)", match[0])[0]
        return (html_attrs, tag_content)


    def _get_html_attrs(self, match):
        attrs = re.search(fr"(?<=<)((.|\n)*?)(?=>)", match[0])[0].split()
        attrs.pop(0)
        return attrs
   
    def __repr__(self) -> str:
        return self.text
    
    def as_html(self):
        return template.render(template=self.template, script = self.script)





def main(vue_fp):
    # return template.render(var="<h1>Hello from base.html</h1>")
    if not vue_fp:
        return None
    vcomp = Vue(vue_fp)
    # print(vcomp.template)
    return vcomp.as_html()
    


if __name__ == "__main__":
    main()
