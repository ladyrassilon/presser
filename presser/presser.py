import requests
from bs4 import BeautifulSoup
import execjs
import re
import urlparse

class Presser():
    def get_data_for_vine_id(self, vine_id):
        page = requests.get("https://vine.co/v/{}".format(vine_id))
        if page.ok:
            content = BeautifulSoup(page.content)
            all_script_tags = content.find_all("script")
            potential_script_tags = [script for script in all_script_tags if not script.has_attr("src")]
            script_lines = []
            for tag in potential_script_tags:
                for content in tag.contents:
                    for line in content.split(";\n"):
                        if line.count("window.POST_DATA"):
                            script_lines.append(line.replace("window.POST_DATA = ", ""))
            if len(script_lines) > 1:
                raise Exception("More post data extracted than expected")
            script_line = script_lines[0].replace("POST = ","")
            data = execjs.eval(script_line)
            vine = data[vine_id]
            return vine
        else:
            raise Exception(msg="{} - {}".format(page.status_code,page.content))
    def get_data_for_vine_from_url(self, url):
        parsed_url = urlparse.urlparse(url)
        if parsed_url.netloc == "vine.co":
            results = re.search('/v/(?P<vine_id>\w+)',parsed_url.path)
            try:
                vine_id = results.group("vine_id")
                return self.get_data_for_vine_id(vine_id)
            except IndexError:
                raise Exception(msg="{} does not contain a valid vine id".format(parsed_url.path))
        else:
            raise Exception(msg="{} is not a valid vine domain".format(parsed_url.netloc))