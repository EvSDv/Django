from django.shortcuts import render
from django.views.generic import TemplateView
import csv


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        with open('inflation_russia.csv', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            table = list()
            for row in reader:
                row_list = list()
                for item in row:
                    if item:
                        row_list.append(item)
                    else:
                        row_list.append('-')
                table.append(row_list)
            head = table[0]
            table = table[1:]
            context = {'head': head,
                       'table': table}

        return render(request, self.template_name,
                      context)
