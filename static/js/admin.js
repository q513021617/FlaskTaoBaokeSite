$(function(){
$('#batchGetGoods').click(function () {
  var $btn = $(this)
  $btn.button('loading');
  batchGetgoods($btn)
});



function batchGetgoods(btn) {
    var progress = $.AMUI.progress;
    progress.start();
    $.get("/admin/batchGetGoods",{},function(result){
        btn.button('reset');
        progress.done();
  });
}

});

function addGood(){

    location.href="/admin/addgoods"
}