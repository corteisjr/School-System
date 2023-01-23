$(document).ready(function(){
    
    var deleteBtn = $('.delete-btn');
    $(deleteBtn).on('click', function(e) {
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar este Aluno?');

        if(result){
            window.location.href = delLink;
        }
    });
})