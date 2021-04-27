# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
from sys import argv
import yaml


def gen_template(template_j2, data_yml):
    """
    Создает шаблон
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
    # Для запуска скрипта без аргументов:
    # print(gen_template("main.j2", "data/eltex/ltp4x.yml"))
    #
    # Для запуска скрипта через аргументы:
    # template = argv[1]
    # data = argv[2]
    # print(gen_template(template, data))