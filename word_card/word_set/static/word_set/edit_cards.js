function addRow(){
    let div = document.createElement("div")
    div.innerHTML = '<div>' +
    '<label for="word">英文</label>' + ' ' +
    '<input type="text" name="word" required="required"> ' + ' ' +
    '<label for="chinese">中文</label>' + ' ' +
    '<input type="text" name="chinese" required="required">' + ' ' +
    '<button onclick="delete_word(event)" class="btn bg-warning m-2">刪除</button>' +
    '</div>'
    document.getElementById("filedSpace").appendChild(div)
}
function delete_word(e){
let file = e.target.parentNode.parentNode
let del_div = e.target.parentNode
file.removeChild(del_div)
}