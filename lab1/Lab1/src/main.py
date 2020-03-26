from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lxml import etree
import os
import webbrowser


def cleanup():
    try:
        os.remove("../results/golos.xml")
        os.remove("../results/petmarket.xml")
        os.remove("../results/petmarket.xhtml")
    except OSError:
        pass


def scrap_data():
    process = CrawlerProcess(get_project_settings())
    process.crawl('golos')
    process.crawl('petmarket')
    process.start()


def print_average():
    root = etree.parse("../results/golos.xml")
    pages = root.xpath("//page")
    count = 0
    sum_of_fragments = 0
    for page in pages:
        count = count + 1
        sum_of_fragments = sum_of_fragments + page.xpath("count(fragment[@type='text'])")
    print("Average quantity: %d" % (sum_of_fragments / count))


def make_result_page():
    transform = etree.XSLT(etree.parse("petmarket.xsl"))
    result = transform(etree.parse("../results/petmarket.xml"))
    result.write("../results/petmarket.xhtml", pretty_print=True, encoding="UTF-8")
    webbrowser.open('file://' + os.path.realpath("../results/petmarket.xhtml"))


if __name__ == '__main__':
    cleanup()
    scrap_data()
    print("Scraping finished")
    while True:
        print("*" * 50)
        print("1 [Average value of text elements on golos.ua]")
        print("2 [Page with products]")
        print("> ", end='', flush=True)
        number = input()
        if number == "1":
            print_average()
        elif number == "2":
            make_result_page()
        else:
            break
