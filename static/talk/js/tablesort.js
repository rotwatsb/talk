window.onload = function() {
    var table = document.getElementById("sorttable");
    for (var i = 0; i < table.rows[0].cells.length; i++) {
	table.rows[0].cells[i].addEventListener("click", function() {
	    this.sortasc = this.sortasc ? false : true;
	    sorttablebycol(table, this.cellIndex, this.sortasc ? gtr : lss);
	});
    }
}

function mycmp(table, a, b, col, cmp) {
    c1 = parseInt(table.rows[a].cells[col].innerHTML);
    c2 = parseInt(table.rows[b].cells[col].innerHTML);

    if (c1 == NaN || c2 == NaN) {
	c1 = table.rows[a].cells[col].innerHTML;
	c2 = table.rows[b].cells[col].innerHTML;
    }
    return cmp(c1, c2);
}

function gtr(c1, c2) {
    return (c1 > c2);
}

function lss(c1, c2) {
    return (c1 < c2);
}

function sorttablebycol(table, col, cmp) {
    mergesortrows(table, col, cmp, 1, table.rows.length - 1);
}

function mergesortrows(table, col, cmp, left, right) {
    if (right - left > 0) {
	var mid = Math.floor((left + right) / 2);
	mergesortrows(table, col, cmp, left, mid);
	mergesortrows(table, col, cmp, mid + 1, right);
	merge(table, col, cmp, left, mid, mid + 1, right);
    }
}

function merge(table, col, cmp, l1, l2, r1, r2) {
    var low = l1;
    var merged = [];
    while (l1 <= l2 || r1 <= r2) {
	if (r1 > r2 || (l1 <= l2 && mycmp(table, l1, r1, col, cmp))) {
	    merged.push(table.rows[l1]);
	    l1++;
	}
	else if (l1 > l2 || (r1 <= r2 && !mycmp(table, l1, r1, col, cmp))) {
	    merged.push(table.rows[r1]);
	    r1++;
	}
    }
    var last = r2 + 1 < table.rows.length ? table.rows[r2 + 1] : null;
    for (var i = 0; i < merged.length; i++) {
	var parent = merged[i].parentNode;
	parent.removeChild(merged[i]);
	if (last) {
	    parent.insertBefore(merged[i], last);
	}
	else {
	    parent.appendChild(merged[i]);
	}
    }
}

