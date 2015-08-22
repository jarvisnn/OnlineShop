function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires + "; path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}

function resetCookie() {
    setCookie('items', '', 1000);
    setCookie('numberOfItems', '', 1000);
}

function addNewItem(id) {
    if (getCookie("items").indexOf('-'+id+'-') == -1) {
        if (getCookie("numberOfItems") == "NaN" || getCookie("numberOfItems") == "") {
            setCookie("numberOfItems", 1, 1000)
        } else {
            setCookie("numberOfItems", parseInt(getCookie("numberOfItems")) + 1, 1000)
        }
        setCookie("items", getCookie("items") + '-' + id + '-', 1000)
    }
    refreshCart();
}

function deleteItem(id) {
    var items = getCookie("items");
    if (items.indexOf('-' + id + '-') != -1) {
        setCookie("items",  items.replace('-' + id + '-', ''),1000)
        setCookie("numberOfItems", parseInt(getCookie("numberOfItems")) - 1, 1000)
    }
    location.reload();
}

function refreshCart() {
    var currentCart = getCookie("numberOfItems");
    if (currentCart != "" && currentCart != 0) {
        $("#badge").slideUp();
        $("#badge").html(currentCart);
        $("#badge").slideDown();
    }
}

function increaseSL(id) {
    var key = 'sl-' + id;
    var value = parseInt($('#'+key).text());
    value++;
    $('#'+key).text(value);
    refreshCost();
}

function decreaseSL(id) {
    var key = 'sl-' + id;
    var value = parseInt($('#'+key).text());
    value = Math.max(value-1, 1);
    $('#'+key).text(value);
    refreshCost();
}

function refreshCost() {
    var str = getCookie('items');
    var list = str.split('-');
    var cost = 0.0;

    for (var i in list) {
        var id=list[i];
	if ($('#price-'+id).length == 0) {
	    if (id != '') {
		deleteItem(id);
            }
	} else {
            cost += parseFloat($('#price-'+id).text().replace(',','')) * parseFloat($('#sl-'+id).text());
        }
    }

    $('#total-cost').text(cost.format());
}

$(document).ready(function() {
    refreshCart();
    if ($('#total-cost').length != 0) {
        refreshCost();
    }
});

$('#order-form').on('submit', function(event) {
    event.preventDefault();

    var value = ""
    var str = getCookie('items');
    var list = str.split('-');

    for (var i in list) {
        var id=list[i];
        if (id != '') {
            value += '[' + id + '-' + $('#product-name-'+id).text() + '-slượng '+ $('#sl-'+id).text() + '] ';
        }
    }

    $('#order-products').val(value);
    $('#cost').val($('#total-cost').text().replace(',',''));
    this.submit();
});

Number.prototype.format = function(n, x) {
    var re = '\\d(?=(\\d{' + (x || 3) + '})+' + (n > 0 ? '\\.' : '$') + ')';
    return this.toFixed(Math.max(0, ~~n)).replace(new RegExp(re, 'g'), '$&,');
};
