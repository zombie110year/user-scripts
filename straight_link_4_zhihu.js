// ==UserScript==
// @name         Zhihu Straight Link
// @namespace    zombie110year
// @version      0.1
// @description  去掉知乎跳转链接前的 link.zhihu....
// @author       Zombie110year
// @match        https://*.zhihu.com/*
// @grant        none
// ==/UserScript==
//! 未知 BUG, 只修改了第一个链接.
/**
 * 知乎外链前缀
 * 注意正则表达式中的 \. [?] 分别表示 点号, 问号. 问号不能用反斜杠转义, 因此写进
 * 字符集中.
 */
var gPATTERN = RegExp("^http://link\.zhihu\.com/[?]target=(.+)$", "gi");
// 知乎外链元素的 CSS 选择器
var gSELECTOR = "a.wrap.external";

(function () {
    'use strict';
    rewriteLinks();
})();


/**
 * 传入获取到的元素, 返回直链地址
 * :para element: HTML 元素 a
 * :return: String, 直链地址
 */
function getLink(element) {
    var raw_link;
    var link;

    raw_link = element.getAttribute('href');
    link = gPATTERN.exec(raw_link)[1];
    link = decodeURIComponent(link);
    return link;
}

/**
 * 获取文档中所有符合条件的元素
 *
 * :param selector: css 选择器
 * :return: Array, 存储了所有符合条件的元素.
 */
function getLinkElement(selector) {
    var links;
    links = document.querySelectorAll(selector);
    return links;
}

/**
 * 根据获取到的元素与提取到的链接地址, 修改原元素
 */
function rewriteLinks() {
    var elements = getLinkElement(gSELECTOR);

    let element;
    for (element of elements) {
        let link = getLink(element);
        element.setAttribute('href', link);
    }
}