function sellDetails(id_vehicle){
    $.ajax({
        type: "GET",
        url: '/api/vehicles/'+id_vehicle,
        success: function(response){
            document.getElementById('modelo-venda').textContent = response.modelo
            document.getElementById('marca-venda').textContent = response.marca
            document.getElementById('cor-venda').textContent = response.cor
            document.getElementById('placa-venda').textContent =
                response.placa
            document.getElementById('valor_compra-venda').textContent = new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL',
          }).format(response.valor_compra)


            document.getElementById('ano-venda').textContent =
                response.ano_fabricacao

            document.getElementById('chassi-venda').textContent =
                response.chassi

            document.getElementById('data_compra-venda').textContent =
                response.data_compra

            document.getElementById('data_venda-venda').textContent =
                response.data_venda

            document.getElementById('valor_venda-venda').textContent = new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL',
          }).format(response.valor_venda)

            document.getElementById('lucro_prejuizo-venda').textContent =
                new Intl.NumberFormat('pt-BR', {
                    style: 'currency',
                    currency: 'BRL',
                  }).format(response.valor_venda - response.valor_compra)

            if(response.valor_venda - response.valor_compra > 0) {
                comissao = 0.1 * (response.valor_venda - response.valor_compra)
            }else{
                comissao = 0
            }
            document.getElementById('comissao-venda').textContent =
                new Intl.NumberFormat('pt-BR', {
                    style: 'currency',
                    currency: 'BRL',
                  }).format(comissao)
        },
        dataType: 'json'
    });
}

function cancelSell(id_vehicle){
        data = {
            valor_venda: null,
            data_venda: null,
        }

        $.ajax({
            type: "PATCH",
            url: '/api/vehicles/'+id_vehicle+'/',
            data: data,
            success: function (response) {
                console.log(response.status)
                document.location.reload(true);

            },
            error: function (response) {
                alert('Erro ao cancelar venda de veículo!')
            },
            dataType: 'json'
        });
}

$(document).ready(function() {
    $('#form-modal').on('submit', function(e){

        e.preventDefault();
        data = {
            modelo: document.getElementById('modelo').value,
            marca: document.getElementById('marca').value,
            cor: document.getElementById('cor').value,
            placa: document.getElementById('placa').value,
            valor_compra: document.getElementById('valor_compra').value,
            valor_venda: document.getElementById('valor_venda').value,
            chassi: document.getElementById('chassi').value,
            ano_fabricacao: document.getElementById('ano_fabricacao').value,
            data_compra: document.getElementById('data_compra').value,
            data_venda: document.getElementById('data_venda').value,
        }

        $.ajax({
            type: "PUT",
            url: '/api/vehicles/'+update_id_vehicle+'/',
            data: data,
            success: function (response) {
                document.location.reload(true);
            },
            error: function (response) {
                alert('Erro ao editar venda de veículo!')
            },
            dataType: 'json'
        });
    });
});


function updateModal(id_vehicle){
    update_id_vehicle = id_vehicle
    modal_btn = document.getElementById('modal-btn')

    $.ajax({
        type: "GET",
        url: '/api/vehicles/'+id_vehicle,
        success: function(response){
            document.getElementById('modelo').value = response.modelo
            document.getElementById('marca').value = response.marca
            document.getElementById('cor').value = response.cor
            document.getElementById('placa').value = response.placa
            document.getElementById('chassi').value = response.chassi
            document.getElementById('valor_compra').value = response.valor_compra
            document.getElementById('valor_venda').value = response.valor_venda
            dt_compra = response.data_compra.split('/')[2]+'-'+response.data_compra.split('/')[1]+'-'+response.data_compra.split('/')[0]
            dt_venda = response.data_venda.split('/')[2]+'-'+response.data_venda.split('/')[1]+'-'+response.data_venda.split('/')[0]
            document.getElementById('data_compra').value = dt_compra
            document.getElementById('data_venda').value = dt_venda
            document.getElementById('ano_fabricacao').value = response.ano_fabricacao
        },
        dataType: 'json'
    });
}

$(document).ready(function () {
    $('#dtHorizontalVerticalExample').DataTable({
    "scrollX": true,
    "scrollY": 250,
    "bLengthChange": false,
      "language":
      {
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

    });
    $('.dataTables_length').addClass('bs-select');
});