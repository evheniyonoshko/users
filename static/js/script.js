function hide_show() {
    var add_btn = document.getElementById('add_btn');
    var label_course = document.getElementById('label_course');
    var block = document.getElementById('id_courses');
    if (block.style.display === 'none' && ($("#selected-items > div.empty").length > 0)) {
        block.style.display = 'inline-block';
        label_course.style.display = 'inline-block'
        add_btn.style.marginLeft = '25px';
        add_btn.setAttribute('onclick','add_selecded_course()');
    } else {
        if ($("#selected-items > div.empty").length > 0) {
            block.style.display = 'inline-block';
            label_course.style.display = 'inline-block'
            add_btn.style.marginLeft = '25px';
        }
        else {
            block.style.display = 'none';
            label_course.style.display = 'none'
            add_btn.style.marginLeft = '205px';
        }
    }
}

function add_selecded_course() {
    var selectobject = document.getElementById("id_courses");
    if (selectobject.value != ''){
        var n = $("#selected-items > div.empty").length;
        var id_item = "selected-item-" + n;
        var id_item_name = "course-name-" + n;
        var element = document.getElementById(id_item);
        element.classList.remove("empty");
        element.classList.add('not-empty');
        var name = document.getElementById(id_item_name);
        element.style.display = 'block';
        name.textContent = selectobject.value;
        for (var i=1; i<selectobject.length; i++){
            if (selectobject.options[i].value == selectobject.value)
                selectobject.remove(i);
        }
        if ($("#selected-items > div.empty").length < 1) {
            hide_show();
        };
    };
}

function del(elem) {
    var selectobject = document.getElementById("id_courses");
    var element = document.getElementById($(elem).parent().closest('div').attr('id'));
    var id_item_name = "course-name-" + ($(elem).parent().closest('div').attr('id')).slice(-1);
    var name = document.getElementById(id_item_name);
    var opt = document.createElement('option');
    element.classList.add('empty');
    element.classList.remove("not-empty");
    element.style.display = 'none';
    var option = document.createElement("option");
    option.text = name.textContent;
    option.value = name.textContent;
    selectobject.appendChild(option);
    
    if ($("#selected-items > div.empty").length > 0) {
        hide_show();
    }
}
