# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml


def gen_template(template_j2, data_yml):
    """
    Создает блок шаблона
    :param template_j2: Файл с J2 шаблоном
    :param data_yml: Файл с данными в виде папка/файл
    :return: строка с шаблоном
    """

    dir_j2 = "j2-templates"

    env = Environment(loader=FileSystemLoader(dir_j2),
                      trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_j2)

    with open(data_yml) as yml:
        data = yaml.safe_load(yml)

    return template.render(data)


if __name__ == '__main__':
    print(
#        gen_template("applications.j2", "data/eltex/ltp8x/applications.yml"),
#        gen_template("items.j2", "data/eltex/ltp8x/items.yml"),
        gen_template("graphs.j2", "data/eltex/ltp8x/graphs.yml")
    )
