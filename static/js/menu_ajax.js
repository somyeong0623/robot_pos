// 결제 완료버튼을 누를시 장바구니(포스창 오른쪽의 주문내역)에서
// 메뉴리스트의 메뉴이름, 메뉴 수량을 받아와서 데이터베이스에 삽입
// 이때, initial page에서 넘겨받은 table_no과, o_id를 기준으로 해당 doc의 menu리스트에 값을 추가한다.

// function listing() {
//     $.ajax({
//         type: "GET",
//         url: "/pos?sample_give=샘플데이터",
//         data: {},
//         success: function (response) {
//             alert(response['msg'])
//         }
//     })
// }
//

var table_no = getUrlVars()["table_number"];

function payment() {
    let list = [];
    $('#menu_list tr').each(function () {
        var tr = $(this);
        var td = tr.children();
        let menu_name = td.find('.menu_name').text();
        let menu_count = td.find('.menu_count').text();
        console.log(menu_name, menu_count);
        list.push({"name": menu_name,"count": menu_count});
    });
    console.log(table_no);
    console.log(list);

    $.ajax({
        type: "POST",
        url: "/payment",
        data: {menulist_give:list},
        success: function (response) {
            alert(response['msg'])
        }
    })

}