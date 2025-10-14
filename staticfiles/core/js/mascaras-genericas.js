$(document).ready(function () {
    // Initialize all masks
    $('.mask_cpf').mask('000.000.000-00', {placeholder: ""});
    $('.mask_data').mask('00/00/0000', {placeholder: ""});
    $('.mask_data_hora').mask('00/00/0000 00:00', {placeholder: ""});
    $('.mask_cep').mask('00000-000', {placeholder: ""});
    $('.mask_tel_fixo').mask('(00) 0000-0000', {placeholder: ""});
    $('.mask_tel_celular').mask('(00) 00000-0000', {placeholder: ""});
    
    // For international numbers use:
    $('.mask_tel_celular_internacional').mask('+00 00 00000-0000', {placeholder: ""});
    
    // CNPJ pattern
    $('.mask_cnpj').mask('00.000.000/0000-00', {placeholder: ""});
});