function updateDashboard(){
    interval = document.querySelector("#time-interval").value
    $.ajax({
        type: "GET",
        url: '/api/profits?interval='+interval,
        success: function(response){
            document.getElementById('total_compras').textContent = response.total_compras
            document.getElementById('total_vendas').textContent = response.total_vendas
            document.getElementById('lucro_prejuizo_total').textContent = response.lucro_prejuizo_total
            document.getElementById('total_comissoes').textContent = response.total_comissoes
        },
        dataType: 'json'
    });

}

$(document).ready(function () {
    language = {
        "emptyTable": "Não foi encontrado nenhum registro",
        "loadingRecords": "A carregar...",
        "processing": "A processar...",
        "lengthMenu": "Mostrar _MENU_ registros",
        "zeroRecords": "Não foram encontrados resultados",
        "search": "Procurar:",
        "paginate": {
            "first": "Primeiro",
            "previous": "Anterior",
            "next": "Seguinte",
            "last": "Último"
        },
        "aria": {
            "sortAscending": ": Ordenar colunas de forma ascendente",
            "sortDescending": ": Ordenar colunas de forma descendente"
        },
        "autoFill": {
            "cancel": "cancelar",
            "fill": "preencher",
            "fillHorizontal": "preencher células na horizontal",
            "fillVertical": "preencher células na vertical",
            "info": "Exemplo de Auto Preenchimento"
        },
        "buttons": {
            "collection": "Coleção",
            "colvis": "Visibilidade de colunas",
            "colvisRestore": "Restaurar visibilidade",
            "copy": "Copiar",
            "copyKeys": "Pressiona CTRL ou u2318 + C para copiar a informação para a área de transferência. Para cancelar, clica neste mensagem ou pressiona ESC.",
            "copySuccess": {
                "1": "Uma linha copiada para a área de transferência",
                "_": "%ds linhas copiadas para a área de transferência"
            },
            "copyTitle": "Copiar para a área de transferência",
            "csv": "CSV",
            "excel": "Excel",
            "pageLength": {
                "-1": "Mostrar todas as linhas",
                "1": "Mostrar 1 linha",
                "_": "Mostrar %d linhas"
            },
            "pdf": "PDF",
            "print": "Imprimir"
        },
        "decimal": ",",
        "infoFiltered": "(filtrado num total de _MAX_ registros)",
        "infoThousands": ".",
        "searchBuilder": {
            "add": "Adicionar condição",
            "button": {
                "0": "Construtor de pesquisa",
                "_": "Construtor de pesquisa (%d)"
            },
            "clearAll": "Limpar tudo",
            "condition": "Condição",
            "conditions": {
                "date": {
                    "after": "Depois",
                    "before": "Antes",
                    "between": "Entre",
                    "empty": "Vazio",
                    "equals": "Igual",
                    "not": "Diferente",
                    "notBetween": "Não está entre",
                    "notEmpty": "Não está vazio"
                },
                "number": {
                    "between": "Entre",
                    "empty": "Vazio",
                    "equals": "Igual",
                    "gt": "Maior que",
                    "gte": "Maior ou igual a",
                    "lt": "Menor que",
                    "lte": "Menor ou igual a",
                    "not": "Diferente",
                    "notBetween": "Não está entre",
                    "notEmpty": "Não está vazio"
                },
                "string": {
                    "contains": "Contém",
                    "empty": "Vazio",
                    "endsWith": "Termina em",
                    "equals": "Igual",
                    "not": "Diferente",
                    "notEmpty": "Não está vazio",
                    "startsWith": "Começa em"
                },
                "array": {
                    "equals": "Igual",
                    "empty": "Vazio",
                    "contains": "Contém",
                    "not": "Diferente",
                    "notEmpty": "Não está vazio",
                    "without": "Não contém"
                }
            },
            "data": "Dados",
            "deleteTitle": "Excluir condição de filtragem",
            "logicAnd": "E",
            "logicOr": "Ou",
            "title": {
                "0": "Construtor de pesquisa",
                "_": "Construtor de pesquisa (%d)"
            },
            "value": "Valor"
        },
        "searchPanes": {
            "clearMessage": "Limpar tudo",
            "collapse": {
                "0": "Painéis de pesquisa",
                "_": "Painéis de pesquisa (%d)"
            },
            "count": "{total}",
            "countFiltered": "{shown} ({total})",
            "emptyPanes": "Sem painéis de pesquisa",
            "loadMessage": "A carregar painéis de pesquisa",
            "title": "Filtros ativos"
        },
        "select": {
            "1": "%d linha seleccionada",
            "_": "%d linhas seleccionadas",
            "cells": {
                "1": "1 célula seleccionada",
                "_": "%d células seleccionadas"
            },
            "columns": {
                "1": "1 coluna seleccionada",
                "_": "%d colunas seleccionadas"
            },
            "rows": {
                "1": "%d linha seleccionada"
            }
        },
        "thousands": ".",
        "editor": {
            "close": "Fechar",
            "create": {
                "button": "Novo",
                "title": "Criar novo registro",
                "submit": "Criar"
            },
            "edit": {
                "button": "Editar",
                "title": "Editar registro",
                "submit": "Atualizar"
            },
            "remove": {
                "button": "Remover",
                "title": "Remover",
                "submit": "Remover"
            },
            "error": {
                "system": "Um erro no sistema ocorreu"
            },
            "multi": {
                "title": "Multiplos valores",
                "info": "Os itens selecionados contêm valores diferentes para esta entrada. Para editar e definir todos os itens para esta entrada com o mesmo valor, clique ou toque aqui, caso contrário, eles manterão seus valores individuais.",
                "restore": "Desfazer alterações"
            }
        },
        "info": "Mostrando os registros _START_ a _END_ num total de _TOTAL_",
        "infoEmpty": "Mostrando 0 os registros num total de 0"
    }
    $('#dtHorizontalVerticalExample2').DataTable({
    "scrollX": true,
    "scrollY": 250,
    "bLengthChange": false,
      "language": language
    });
    $('.dataTables_length').addClass('bs-select');

});