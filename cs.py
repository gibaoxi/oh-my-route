/**
 * YouTube  : https://youtube.com/@am_clubs
 * Telegram : https://t.me/am_clubs
 * GitHub   : https://github.com/amclubs
 * BLog     : https://amclubss.com
 */

let id = base64Decode('ZWM4NzJkOGYtNzJiMC00YTA0LWI2MTItMDMyN2Q4NWUxOGVk');
let uuid;
let host;

let paddr;

let s5 = '';
let socks5Enable = false;
let parsedSocks5 = {};

let ipLocal = [
    'wto.org:443#youtube.com/@am_clubs 数字套利(视频教程)',
    'icook.hk#t.me/am_clubs TG群(加入解锁更多节点)',
    'time.is#github.com/amclubs GitHub仓库(关注查看新功能)',
    '127.0.0.1:1234#amclubss.com 博客教程(cfnat)'
];
let proxyIPsAll = []; // 存储所有可用的代理IP
let currentProxyIndex = 0; // 当前代理IP索引

// 加载代理IP列表的函数
async function loadProxyIPs(env) {
    try {
        // 从KV获取代理IP列表
        const existingProxy = await loadFromKV(env, base64Decode('Y2ZfcHJveHlfaXA='));
        if (existingProxy && existingProxy.trim().length > 0) {
            proxyIPsAll = existingProxy.split('\n').map(v => v.trim()).filter(v => v).map(v => v.split('#')[0]).map(v => v.trim()).filter(v => v);
        }
        
        // 如果没有配置代理IP，使用默认值
        if (proxyIPsAll.length === 0) {
            proxyIPsAll = [
                'proxy1.amclubs.com',
                'proxy2.amclubs.com', 
                'proxy3.amclubs.com',
                'proxy4.amclubs.com',
                'proxy5.amclubs.com'
            ];
        }
        
        log(`Loaded ${proxyIPsAll.length} proxy IPs: ${proxyIPsAll.join(', ')}`);
    } catch (err) {
        errorLogs('Failed to load proxy IPs:', err);
        proxyIPsAll = [];
    }
}
const defaultIpUrlTxt = base64Decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2FtY2x1YnMvYW0tY2YtdHVubmVsL21haW4vZXhhbXBsZS9pcHY0LnR4dA==');
let randomNum = 25;
let ipUrlTxt = [defaultIpUrlTxt];
let ipUrlCsv = [];
let noTLS = false;
let sl = 5;

let fakeUserId;
let fakeHostName;

let isBase64 = true;
let subConfig = base64Decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2FtY2x1YnMvQUNMNFNTUi9tYWluL0NsYXNoL2NvbmZpZy9BQ0w0U1NSX09ubGluZV9GdWxsX011bHRpTW9kZS5pbmk=');
let subConverter = base64Decode('dXJsLnYxLm1r');
let subProtocol = 'https';

let subUpdateTime = 6;
let timestamp = 4102329600000;
let total = 99 * 1125899906842624;
let download = Math.floor(Math.random() * 1099511627776);
let upload = download;
let expire = Math.floor(timestamp / 1000);

let nat64 = true;
let nat64Prefix;
let nat64Prefixs = [
    '2602:fc59:b0:64::'
];

const protTypeBase64 = 'ZG14bGMzTT0=';
const protTypeBase64Tro = 'ZEhKdmFtRnU=';
const httpPattern = /^http(s)?:\/\/.+/;
let network = 'ws';
let projectName = base64Decode('YW1jbHVicw==');
let fileName = '5pWw5a2X5aWX5Yip';
let ytName = base64Decode('aHR0cHM6Ly95b3V0dWJlLmNvbS9AYW1fY2x1YnM/c3ViX2NvbmZpcm1hdGlvbj0x');
let tgName = base64Decode('aHR0cHM6Ly90Lm1lL2FtX2NsdWJz');
let ghName = base64Decode('aHR0cHM6Ly9naXRodWIuY29tL2FtY2x1YnMvYW0tY2YtdHVubmVs');
let bName = base64Decode('aHR0cHM6Ly9hbWNsdWJzcy5jb20=');
let pName = '5pWw5a2X5aWX5Yip';
let hostRemark;
let enableLog = false;
let enableOpen = true;

const DEFAULT_TARGET_COUNT = 512;
let nipHost = base64Decode('bmlwLmxmcmVlLm9yZw==');
let extraIp;
let extraIpProxy;

export default {
    async fetch(request, env) {
        try {
            const url = new URL(request.url);
            const headers = request.headers;
            return await mainHandler({ req: request, url, headers, res: null, env });
        } catch (err) {
            errorLogs('Worker Error:', err);
            return new Response('Worker Error: ' + err.message, { status: 500 });
        }
    },
};

// ======= 主逻辑函数（共用） =======
async function mainHandler({ req, url, headers, res, env }) {
    const { ENABLE_LOG, ID, UUID, HOST, SOCKS5, IP_URL, PROXYIP, NAT64, NAT64_PREFIX, HOST_REMARK, PROT_TYPE, RANDOW_NUM, SUB_CONFIG, SUB_CONVERTER, NO_TLS, NIP_HOST, EXTRA_IP, EXTRA_IP_PROXY, ENABLE_OPEN } = env || {};

    const rawHost = headers.get('host') || headers.get('Host') || 'localhost';
    const userAgent = headers.get('User-Agent') || '';
    log(`[mainHandler]-->rawHost: ${rawHost}`);
    const rawEnableLog = url.searchParams.get('ENABLE_LOG') || getEnvVar('ENABLE_LOG', env) || enableLog;
    enableLog = parseBool(rawEnableLog, enableLog);
    const rawEnableOpen = getEnvVar('ENABLE_OPEN', env) || enableOpen;
    enableOpen = parseBool(rawEnableOpen, enableOpen);
    noTLS = url.searchParams.get('NO_TLS') || getEnvVar('NO_TLS', env) || noTLS;

    id = getEnvVar('ID', env) || ID || id;
    uuid = url.searchParams.get('UUID') || getEnvVar('UUID', env) || UUID;
    host = url.searchParams.get('HOST') || getEnvVar('HOST', env) || HOST;
    log(`[mainHandler]-->id: ${id} uuid: ${uuid} host: ${host}`);

    s5 = url.searchParams.get('SOCKS5') || getEnvVar('SOCKS5', env) || SOCKS5 || s5;
    parsedSocks5 = await parseSocks5FromUrl(s5, url);
    if (parsedSocks5) socks5Enable = true;

    let ip_url = url.searchParams.get('IP_URL') || getEnvVar('IP_URL', env) || IP_URL;
    if (ip_url) {
        const result = await parseIpUrl(ip_url);
        ipUrlCsv = result.ipUrlCsvResult;
        ipUrlTxt = result.ipUrlTxtResult;
    }
    const existing = await loadFromKV(env, decodeBase64Utf8('Y2Zfbm9ybWFsX2lw'));
    if (existing && existing.trim().length > 0) {
        ipLocal = existing.split('\n').map(v => v.trim()).filter(v => v);
    }

    let proxyIPsAll = [];
    const proxyIPUrl = url.searchParams.get('PROXYIP') || getEnvVar('PROXYIP', env) || PROXYIP;
    if (proxyIPUrl) {
        if (httpPattern.test(proxyIPUrl)) {
            const proxyIpTxt = await addIpText(proxyIPUrl);
            let ipUrlTxtAndCsv;
            if (proxyIPUrl.endsWith('.csv')) {
                ipUrlTxtAndCsv = await getIpUrlTxtAndCsv(noTLS, null, proxyIpTxt);
            } else {
                ipUrlTxtAndCsv = await getIpUrlTxtAndCsv(noTLS, proxyIpTxt, null);
            }
            const uniqueIpTxt = [...new Set([...ipUrlTxtAndCsv.txt, ...ipUrlTxtAndCsv.csv])];
            proxyIPsAll.push(...uniqueIpTxt);
        } else {
            const proxyIPs = await addIpText(proxyIPUrl);
            proxyIPsAll.push(...proxyIPs);
        }
    }
    const existingProxy = await loadFromKV(env, decodeBase64Utf8('Y2ZfcHJveHlfaXA='));
    if (existingProxy && existingProxy.trim().length > 0) {
        const fromKv = existingProxy.split('\n').map(v => v.trim()).filter(v => v).map(v => v.split('#')[0]).map(v => v.trim()).filter(v => v);
        proxyIPsAll.push(...fromKv);
    }
    proxyIPsAll = [...new Set(proxyIPsAll)];
    if (proxyIPsAll.length > 0) {
        paddr = proxyIPsAll[Math.floor(Math.random() * proxyIPsAll.length)];
    }

    nat64 = url.searchParams.get('NAT64') || getEnvVar('NAT64', env) || NAT64 || nat64;
    const nat64PrefixUrl = url.searchParams.get('NAT64_PREFIX') || getEnvVar('NAT64_PREFIX', env);
    if (nat64PrefixUrl) {
        if (httpPattern.test(nat64PrefixUrl)) {
            const proxyIpTxt = await addIpText(nat64PrefixUrl);
            let ipUrlTxtAndCsv;
            if (nat64PrefixUrl.endsWith('.csv')) {
                ipUrlTxtAndCsv = await getIpUrlTxtAndCsv(noTLS, null, proxyIpTxt);
            } else {
                ipUrlTxtAndCsv = await getIpUrlTxtAndCsv(noTLS, proxyIpTxt, null);
            }
            const uniqueIpTxt = [...new Set([...ipUrlTxtAndCsv.txt, ...ipUrlTxtAndCsv.csv])];
            nat64Prefix = uniqueIpTxt[Math.floor(Math.random() * uniqueIpTxt.length)];
        } else {
            nat64Prefixs = await addIpText(nat64PrefixUrl);
            nat64Prefix = nat64Prefixs[Math.floor(Math.random() * nat64Prefixs.length)];
        }
    }

    hostRemark = url.searchParams.get('HOST_REMARK') || getEnvVar('HOST_REMARK', env) || hostRemark;
    let protType = url.searchParams.get('PROT_TYPE') || getEnvVar('PROT_TYPE', env);
    if (protType) protType = protType.toLowerCase();
    randomNum = url.searchParams.get('RANDOW_NUM') || getEnvVar('RANDOW_NUM', env) || randomNum;
    log(`[handler]-->randomNum: ${randomNum}`);

    subConfig = getEnvVar('SUB_CONFIG', env) || SUB_CONFIG || subConfig;
    subConverter = getEnvVar('SUB_CONVERTER', env) || SUB_CONVERTER || subConverter;
    let subProtocol, subConverterWithoutProtocol;
    if (subConverter.startsWith("http://") || subConverter.startsWith("https://")) {
        [subProtocol, subConverterWithoutProtocol] = subConverter.split("://");
    } else {
        [subProtocol, subConverterWithoutProtocol] = [undefined, subConverter];
    }
    subConverter = subConverterWithoutProtocol;
    nipHost = getEnvVar('NIP_HOST', env) || nipHost;
    extraIp = getEnvVar('EXTRA_IP', env) || extraIp;
    extraIpProxy = getEnvVar('EXTRA_IP_PROXY', env) || extraIpProxy;

    fakeUserId = await getFakeUserId(uuid);
    fakeHostName = getFakeHostName(rawHost, noTLS);
    log(`[handler]-->fakeUserId: ${fakeUserId}`);

    // ---------------- 路由 ----------------
    if (url.pathname === `/setting` && !enableOpen) {
        const html = await getSettingHtml(rawHost);
        return sendResponse(html, userAgent, res);
    }
    if (url.pathname === "/login") {
        const result = await login(req, env, res);
        return result;
    }
    if (url.pathname === `/${id}/setting`) {
        const html = await getSettingHtml(rawHost);
        return sendResponse(html, userAgent, res);
    }
    if (url.pathname === `/${id}`) {
        const html = await getConfig(rawHost, uuid, host, paddr, parsedSocks5, userAgent, url, protType, nat64, hostRemark);
        return sendResponse(html, userAgent, res);
    }
    if (url.pathname === `/${fakeUserId}`) {
        const html = await getConfig(rawHost, uuid, host, paddr, parsedSocks5, 'CF-FAKE-UA', url, protType, nat64, hostRemark);
        return sendResponse(html, 'CF-FAKE-UA', res);
    }
    // ✅
    if (url.pathname === `/${id}/ips`) {
        const html = await htmlPage();
        return sendResponse(html, userAgent, res);
    }
    if (url.pathname === '/ipsFetch') {
        const ipSource = url.searchParams.get('ipSource');
        const port = url.searchParams.get('port') || '443';
        nipHost = getNipHost(nipHost);
        log(`[handler]-->nipHost: ${nipHost}`);
        let ipData = await loadIpSource(ipSource, port);
        log('ipData type:', typeof ipData, ipData);
        if (ipData instanceof Response) {
            ipData = await ipData.text();
        }
        if (Array.isArray(ipData)) {
            return new Response(JSON.stringify({ ips: ipData.filter(l => l) }), {
                headers: { 'Content-Type': 'application/json' }
            })
        }
        return new Response(JSON.stringify({ ips: ipData.split('\n').filter(l => l) }), {
            headers: { 'Content-Type': 'application/json' }
        })
    }
    if (url.pathname === `/${id}/save`) {
        try {
            const body = await readJsonBody(req);
            log("[handler]--> save body: ", body);
            const { key, items } = body;
            await saveToKV(env, key, items);
            return sendResponse(JSON.stringify({ ok: true }), userAgent, res);
        } catch (e) {
            return sendResponse(JSON.stringify({ ok: false, error: e.message || String(e) }), userAgent, res, 500);
        }
    }
    if (url.pathname === `/${id}/append`) {
        try {
            const body = await readJsonBody(req);
            const { key, items } = body;
            await appendToKV(env, key, items);
            return sendResponse(JSON.stringify({ ok: true }), userAgent, res);
        } catch (e) {
            return sendResponse(JSON.stringify({ ok: false, error: e.message || String(e) }), userAgent, res, 500);
        }
    }
    if (url.pathname === `/${id}/load`) {
        try {
            let body = {};
            try {
                body = await readJsonBody(req);
            } catch (e) {
                return sendResponse(JSON.stringify({ ok: false, error: "Invalid JSON body" }), userAgent, res, 400);
            }
            if (!body.key) {
                return sendResponse(JSON.stringify({ ok: false, error: "Missing key" }), userAgent, res, 400);
            }
            const value = await loadFromKV(env, body.key);
            if (!value) {
                return sendResponse(JSON.stringify({ ok: false, error: "KV key not found" }), userAgent, res, 404);
            }
            return sendResponse(JSON.stringify({ ok: true, value }), userAgent, res);
        } catch (err) {
            return sendResponse(JSON.stringify({ ok: false, error: err.message }), userAgent, res, 500);
        }
    }
    return login(req, env, res);
}

/** --------------------- main ------------------------------ */
function getEnvVar(key, env) {
    if (env && typeof env[key] !== 'undefined') {
        return env[key];
    }
    if (typeof process !== 'undefined' && process.env && typeof process.env[key] !== 'undefined') {
        return process.env[key];
    }
    return undefined;
}

function isCloudflareRuntime(env) {
    const isCFCache = typeof caches !== "undefined" && caches.default;
    const isCFEnv = env && Object.prototype.toString.call(env) === "[object Object]";
    const isNotNode = typeof process === "undefined" || !process.release || process.release.name !== "node";
    if (isCFCache && isCFEnv && isNotNode) {
        log("[isCloudflareRuntime]--> ✅ Cloudflare Runtime");
        return true;
    }
    log("[isCloudflareRuntime]--> ❌ Vercel/Node Runtime");
    return false;
}

function isCloudflareRequest(req) {
    return typeof Request !== 'undefined' && req instanceof Request;
}

async function readJsonBody(req) {
    if (isCloudflareRequest(req)) {
        return await req.json();
    }
    return await new Promise((resolve, reject) => {
        let raw = '';
        req.on('data', chunk => raw += chunk);
        req.on('end', () => {
            try {
                resolve(JSON.parse(raw));
            } catch (e) {
                reject(new Error('Invalid JSON'));
            }
        });
        req.on('error', reject);
    });
}

function parseBool(val, defaultVal = false) {
    if (val === undefined || val === null) return defaultVal;
    if (typeof val === 'boolean') return val;
    if (typeof val === 'string') {
        return ['1', 'true', 'yes', 'on'].includes(val.toLowerCase());
    }
    if (typeof val === 'number') return val === 1;
    return defaultVal;
}

/** ---------------------Tools------------------------------ */
function log(...args) {
    if (!enableLog) {
        return;
    }
    let prefix = '';
    try {
        // ✅ 判断 Cloudflare Worker 环境
        if (typeof WebSocketPair !== 'undefined' && typeof addEventListener === 'function' && typeof caches !== 'undefined') {
            prefix = '[CF]';
        }
        // ✅ 判断 Vercel / Node 环境
        else if (typeof process !== 'undefined' && process.release?.name === 'node') {
            prefix = '[VC]';
        }
        // ✅ 其他未知环境
        else {
            prefix = '[SYS]';
        }
    } catch (e) {
        prefix = '[LOG]';
    }
    const timestamp = new Date().toISOString().replace('T', ' ').split('.')[0];
    console.log(`${prefix} ${timestamp} →`, ...args);
}

function errorLogs(err, extra = {}) {
    let prefix = '';
    try {
        // 判断 Cloudflare Worker 环境
        if (typeof WebSocketPair !== 'undefined' && typeof addEventListener === 'function' && typeof caches !== 'undefined') {
            prefix = '[CF-ERR]';
        }
        // 判断 Vercel / Node.js 环境
        else if (typeof process !== 'undefined' && process.release?.name === 'node') {
            prefix = '[VC-ERR]';
        }
        else {
            prefix = '[SYS-ERR]';
        }
    } catch {
        prefix = '[ERR]';
    }

    const timestamp = new Date().toISOString().replace('T', ' ').split('.')[0];
    if (err instanceof Error) {
        console.error(`${prefix} ${timestamp} →`, err.message, '\nStack:', err.stack, extra);
    } else {
        console.error(`${prefix} ${timestamp} →`, err, extra);
    }
}

function getHeader(req, name) {
    try {
        if (!req || !req.headers) return '';
        // Edge Headers 
        if (typeof req.headers.get === 'function') {
            const v = req.headers.get(name);
            return (v === undefined || v === null) ? '' : String(v);
        }
        // Node.js headers 
        const v2 = req.headers[name.toLowerCase()];
        return (v2 === undefined || v2 === null) ? '' : String(v2);
    } catch (e) {
        errorLogs('getHeader error:', e);
        return '';
    }
}

function sendResponse(content, userAgent = '', res = null, status = 200) {
    if (!status || typeof status !== 'number') status = 200;

    const isMozilla = userAgent.toLowerCase().includes('mozilla');
    const headers = {
        "Content-Type": isMozilla ? "text/html;charset=utf-8" : "text/plain;charset=utf-8",
        "Profile-Update-Interval": `${subUpdateTime}`,
        "Subscription-Userinfo": `upload=${upload}; download=${download}; total=${total}; expire=${expire}`,
    };

    if (!isMozilla) {
        const fileNameAscii = encodeURIComponent(decodeBase64Utf8(fileName));
        headers["Content-Disposition"] = `attachment; filename=${fileNameAscii}; filename*=gbk''${fileNameAscii}`;
    }

    // Node / Vercel Serverless
    if (res) {
        Object.entries(headers).forEach(([k, v]) => res.setHeader(k, v));
        if (typeof res.status === 'function') return res.status(status).send(content);
        if (typeof res.writeHead === 'function') {
            res.writeHead(status, headers);
            res.end(content);
            return;
        }
    }

    // Edge / CF Worker / Vercel Edge
    if (typeof Response !== 'undefined') {
        return new Response(content, { status, headers });
    }

    return content;
}

function base64Encode(input) {
    try {
        return Buffer.from(input, 'utf-8').toString('base64');
    } catch (e) {
        if (typeof btoa === 'function') {
            const utf8 = new TextEncoder().encode(input);
            let binary = '';
            utf8.forEach(b => binary += String.fromCharCode(b));
            return btoa(binary);
        } else {
            throw new Error('Base64 encode not supported in this environment');
        }
    }
}

function base64Decode(input) {
    if (typeof atob === 'function') {
        // Edge Runtime 
        return atob(input);
    } else if (typeof Buffer === 'function') {
        // Node.js
        return Buffer.from(input, 'base64').toString('utf-8');
    } else {
        throw new Error('Base64 decode not supported in this environment');
    }
}

function doubleBase64Decode(input) {
    const first = base64Decode(input);
    return base64Decode(first);
}

function getFileType(url) {
    const baseUrl = url.split('@')[0];
    const extension = baseUrl.match(/\.(csv|txt)$/i);
    if (extension) {
        return extension[1].toLowerCase();
    } else {
        return 'txt';
    }
}

async function addIpText(envAdd) {
    var addText = envAdd.replace(/[	|"'\r\n]+/g, ',').replace(/,+/g, ',');
    //log(addText);
    if (addText.charAt(0) == ',') {
        addText = addText.slice(1);
    }
    if (addText.charAt(addText.length - 1) == ',') {
        addText = addText.slice(0, addText.length - 1);
    }
    const add = addText.split(',');
    // log(add);
    return add;
}

function socks5Parser(socks5) {
    let [latter, former] = socks5.split("@").reverse();
    let username, password, hostname, port;

    if (former) {
        const formers = former.split(":");
        if (formers.length !== 2) {
            throw new Error('Invalid SOCKS address format: authentication must be in the "username:password" format');
        }
        [username, password] = formers;
    }

    const latters = latter.split(":");
    port = Number(latters.pop());
    if (isNaN(port)) {
        throw new Error('Invalid SOCKS address format: port must be a number');
    }

    hostname = latters.join(":");
    const isIPv6 = hostname.includes(":") && !/^\[.*\]$/.test(hostname);
    if (isIPv6) {
        throw new Error('Invalid SOCKS address format: IPv6 addresses must be enclosed in brackets, e.g., [2001:db8::1]');
    }

    //log(`socks5Parser-->: username ${username} \n password: ${password} \n hostname: ${hostname} \n port: ${port}`);
    return { username, password, hostname, port };
}

async function parseSocks5FromUrl(socks5, url) {
    if (/\/socks5?=/.test(url.pathname)) {
        socks5 = url.pathname.split('5=')[1];
    } else if (/\/socks[5]?:\/\//.test(url.pathname)) {
        socks5 = url.pathname.split('://')[1].split('#')[0];
    }

    const authIdx = socks5.indexOf('@');
    if (authIdx !== -1) {
        let userPassword = socks5.substring(0, authIdx);
        const base64Regex = /^(?:[A-Z0-9+/]{4})*(?:[A-Z0-9+/]{2}==|[A-Z0-9+/]{3}=)?$/i;
        if (base64Regex.test(userPassword) && !userPassword.includes(':')) {
            userPassword = atob(userPassword);
        }
        socks5 = `${userPassword}@${socks5.substring(authIdx + 1)}`;
    }

    if (socks5) {
        try {
            return socks5Parser(socks5);
        } catch (err) {
            log(err.toString());
            return null;
        }
    }
    return null;
}

function getRandomItems(arr, count) {
    if (!Array.isArray(arr)) return [];

    const shuffled = [...arr].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}

async function getFakeUserId(userId) {
    const date = new Date().toISOString().split('T')[0];
    const rawString = `${userId}-${date}`;

    const hashBuffer = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(rawString));
    const hashArray = Array.from(new Uint8Array(hashBuffer)).map(b => ('00' + b.toString(16)).slice(-2)).join('');

    return `${hashArray.substring(0, 8)}-${hashArray.substring(8, 12)}-${hashArray.substring(12, 16)}-${hashArray.substring(16, 20)}-${hashArray.substring(20, 32)}`;
}

function getFakeHostName(host, noTLS) {
    if (host.includes(".pages.dev")) {
        return `${fakeHostName}.pages.dev`;
    } else if (host.includes(".workers.dev") || host.includes("notls") || noTLS === 'true') {
        return `${fakeHostName}.workers.dev`;
    }
    return `${fakeHostName}.xyz`;
}

function revertFakeInfo(content, userId, hostName) {
    log(`revertFakeInfo-->: isBase64 ${isBase64} \n content: ${content}`);
    if (isBase64) {
        content = base64Decode(content);
    }
    content = content.replace(new RegExp(fakeUserId, 'g'), userId).replace(new RegExp(fakeHostName, 'g'), hostName);
    if (isBase64) {
        content = base64Encode(content);
    }
    return content;
}

function decodeBase64Utf8(str) {
    const bytes = Uint8Array.from(atob(str), c => c.charCodeAt(0));
    return new TextDecoder('utf-8').decode(bytes);
}

function xEn(plain, key) {
    const encoder = new TextEncoder();
    const p = encoder.encode(plain);
    const k = encoder.encode(key);
    const out = new Uint8Array(p.length);
    for (let i = 0; i < p.length; i++) {
        out[i] = p[i] ^ k[i % k.length];
    }
    return btoa(String.fromCharCode(...out));
}

function xDe(b64, key) {
    const data = Uint8Array.from(atob(b64), c => c.charCodeAt(0));
    const encoder = new TextEncoder();
    const decoder = new TextDecoder();
    const k = encoder.encode(key);
    const out = new Uint8Array(data.length);
    for (let i = 0; i < data.length; i++) {
        out[i] = data[i] ^ k[i % k.length];
    }
    return decoder.decode(out);
}

async function parseIpUrl(ip_url) {
    const newCsvUrls = [];
    const newTxtUrls = [];
    try {
        const response = await fetch(ip_url);
        const text = await response.text();
        const lines = text.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
        const hasHttpLinks = lines.some(line => /^https?:\/\//i.test(line));
        if (hasHttpLinks) {
            lines.forEach(u => {
                if (/^https?:\/\//i.test(u)) {
                    if (getFileType(u) === 'csv') {
                        newCsvUrls.push(u);
                    } else {
                        newTxtUrls.push(u);
                    }
                }
            });
        } else {
            if (getFileType(ip_url) === 'csv') {
                newCsvUrls.push(ip_url);
            } else {
                newTxtUrls.push(ip_url);
            }
        }
        const ipUrlCsvResult = [...new Set(newCsvUrls)];
        const ipUrlTxtResult = [...new Set(newTxtUrls)];
        return { ipUrlCsvResult, ipUrlTxtResult };
    } catch (err) {
        errorLogs('获取 IP_URL 文件内容失败：', err);
        return { ipUrlCsvResult: [], ipUrlTxtResult: [] };
    }
}

/** ---------------------Get data------------------------------ */
let subParams = ['sub', 'base64', 'b64', 'clash', 'singbox', 'sb'];
let portSet_http = new Set([80, 8080, 8880, 2052, 2086, 2095, 2082]);
let portSet_https = new Set([443, 8443, 2053, 2096, 2087, 2083]);

async function getConfig(rawHost, userId, host, proxyIP, parsedSocks5, userAgent, _url, protType, nat64, hostRemark) {
    log(`------------getConfig------------------`);
    log(`userId: ${userId} \n host: ${host} \n proxyIP: ${proxyIP} \n userAgent: ${userAgent} \n _url: ${_url} \n protType: ${protType} \n nat64: ${nat64} \n hostRemark: ${hostRemark} `);

    userAgent = userAgent.toLowerCase();
    let port = 443;
    if (host.includes('.workers.dev')) {
        port = 80;
    }

    if (userAgent.includes('mozilla') && !subParams.some(param => _url.searchParams.has(param))) {
        if (!protType) {
            protType = doubleBase64Decode(protTypeBase64);
        }
        const [v2, clash] = getConfigLink(userId, host, host, port, host, proxyIP, protType, nat64);
        return getHtmlRes(rawHost, proxyIP, socks5Enable, parsedSocks5, host, v2, clash);
    }

    let num = randomNum || 25;
    if (protType && !randomNum) {
        num = num * 2;
    }

    const ipUrlTxtAndCsv = await getIpUrlTxtAndCsv(noTLS, ipUrlTxt, ipUrlCsv, num);

    log(`txt: ${ipUrlTxtAndCsv.txt} \n csv: ${ipUrlTxtAndCsv.csv}`);
    let content = await getConfigContent(rawHost, userAgent, _url, host, fakeHostName, fakeUserId, noTLS, ipUrlTxtAndCsv.txt, ipUrlTxtAndCsv.csv, protType, nat64, hostRemark);

    return _url.pathname === `/${fakeUserId}` ? content : revertFakeInfo(content, userId, host);
}

function getHtmlRes(rawHost, proxyIP, socks5Enable, parsedSocks5, host, v2, clash) {
    const subRemark = `IP_LOCAL/IP_URL`;
    let proxyIPRemark = `PROXYIP: ${proxyIP}`;
    if (socks5Enable) {
        proxyIPRemark = `socks5: ${parsedSocks5.hostname}:${parsedSocks5.port}`;
    }
    let remark = `您的订阅节点由设置变量 ${subRemark} 提供, 当前使用反代是${proxyIPRemark}`;
    if (!proxyIP && !socks5Enable) {
        remark = `您的订阅节点由设置变量 ${subRemark} 提供, 当前没设置反代, 推荐您设置PROXYIP变量或SOCKS5变量或订阅连接带proxyIP`;
    }
    return getConfigHtml(rawHost, remark, v2, clash);
}

function getConfigLink(uuid, host, address, port, remarks, proxyip, protType, nat64) {
    const ep = 'none';
    let pathParm = `&PROT_TYPE=${protType}`;
    if (proxyip) {
        pathParm = pathParm + `&PADDR=${proxyip}`;
    }
    if (nat64) {
        pathParm = pathParm + `&P64=${nat64}`;
    }
    if (nat64Prefix) {
        pathParm = pathParm + `&P64PREFIX=${nat64Prefix}`;
    }
    if (s5) {
        pathParm = pathParm + `&S5=${s5}`;
    }
    let path = `/?ed=2560` + pathParm;
    const fp = 'randomized';
    let tls = ['tls', true];
    if (host.includes('.workers.dev') || host.includes('pages.dev')) {
        path = `/${host}${path}`;
        remarks += ' 请用绑定自定义域名访问再订阅！';
    }

    const v2 = getv2LinkConfig({ protType, host, uuid, address, port, remarks, ep, path, fp, tls });
    const clash = getCLinkConfig(protType, host, address, port, uuid, path, tls, fp);
    return [v2, clash];
}

function getv2LinkConfig({ protType, host, uuid, address, port, remarks, ep, path, fp, tls }) {
    log(`------------getv2LinkConfig------------------`);
    log(`protType: ${protType} \n host: ${host} \n uuid: ${uuid} \n address: ${address} \n port: ${port} \n remarks: ${remarks} \n ep: ${ep} \n path: ${path} \n fp: ${fp} \n tls: ${tls} `);

    let sAndp = `&sni=${host}&fp=${fp}`;
    if (portSet_http.has(parseInt(port))) {
        tls = ['', false];
        sAndp = '';
    }
    const k = 'id';
    const t = xEn(protType, k);
    const u = xEn(uuid, k);
    const a = xEn(address, k);
    const p = xEn(port, k);

    const v2 = `${xDe(t, k)}://${xDe(u, k)}@${xDe(a, k)}:${xDe(p, k)}\u003f\u0065\u006e\u0063\u0072\u0079` + 'p' + `${atob('dGlvbj0=')}${ep}\u0026\u0073\u0065\u0063\u0075\u0072\u0069\u0074\u0079\u003d${tls[0]}&type=${network}&host=${host}&path=${encodeURIComponent(path)}${sAndp}#${encodeURIComponent(remarks)}`;
    return v2;
}

function getCLinkConfig(protType, host, address, port, uuid, path, tls, fp) {
    log(`------------getCLinkConfig------------------`);
    log(`protType: ${protType} \n host: ${host} \n address: ${address} \n port: ${port} \n uuid: ${uuid} \n path: ${path} \n tls: ${tls} \n fp: ${fp} `);
    const k = 'idc';
    const t = xEn(protType, k);
    const u = xEn(uuid, k);
    const a = xEn(address, k);
    const p = xEn(port, k);
    return `- {type: ${xDe(t, k)}, name: ${host}, server: ${xDe(a, k)}, port: ${xDe(p, k)}, password: ${xDe(u, k)}, network: ${network}, tls: ${tls[1]}, udp: false, sni: ${host}, client-fingerprint: ${fp}, skip-cert-verify: true,  ws-opts: {path: ${path}, headers: {Host: ${host}}}}`;
}

async function getConfigContent(rawHost, userAgent, _url, host, fakeHostName, fakeUserId, noTLS, ipUrlTxt, ipUrlCsv, protType, nat64, hostRemark) {
    log(`------------getConfigContent------------------`);
    const uniqueIpTxt = [...new Set([...ipUrlTxt, ...ipUrlCsv])];
    let responseBody;
    log(`[getConfigContent]---> protType: ${protType}`);
    if (!protType) {
        protType = doubleBase64Decode(protTypeBase64);
        const responseBody1 = splitNodeData(uniqueIpTxt, noTLS, fakeHostName, fakeUserId, userAgent, protType, nat64, hostRemark);
        const responseBodyTop = splitNodeData(ipLocal, noTLS, fakeHostName, fakeUserId, userAgent, protType, nat64, hostRemark);
        protType = doubleBase64Decode(protTypeBase64Tro);
        const responseBody2 = splitNodeData(uniqueIpTxt, noTLS, fakeHostName, fakeUserId, userAgent, protType, nat64, hostRemark);
        responseBody = [responseBodyTop, responseBody1, responseBody2].join('\n');
    } else {
        const responseBodyTop = splitNodeData(ipLocal, noTLS, fakeHostName, fakeUserId, userAgent, protType, nat64, hostRemark);
        responseBody = splitNodeData(uniqueIpTxt, noTLS, fakeHostName, fakeUserId, userAgent, protType, nat64, hostRemark);
        responseBody = [responseBodyTop, responseBody].join('\n');
    }
    responseBody = base64Encode(responseBody);

    if (!userAgent.includes(('CF-FAKE-UA').toLowerCase())) {
        const safeHost = (rawHost || '').replace(/^https?:\/\//, '');
        let url = `https://${safeHost}/${fakeUserId}`;
        log(`[getConfigContent]---> url: ${url}`);

        if (isClashCondition(userAgent, _url)) {
            isBase64 = false;
            url = createSubConverterUrl('clash', url, subConfig, subConverter, subProtocol);
        } else if (isSingboxCondition(userAgent, _url)) {
            isBase64 = false;
            url = createSubConverterUrl('singbox', url, subConfig, subConverter, subProtocol);
        } else {
            return responseBody;
        }
        try {
            const finalUrl = new URL(url).toString();
            log(`[getConfigContent] Fetching from: ${finalUrl}`);
            const response = await fetch(finalUrl, {
                headers: {
                    'User-Agent': `${userAgent} ${projectName}`
                }
            });
            responseBody = await response.text();
        } catch (err) {
            errorLogs(`[getConfigContent][fetch error] ${err.message}`);
        }
    }

    return responseBody;
}

function createSubConverterUrl(target, url, subConfig, subConverter, subProtocol) {
    return `${subProtocol}://${subConverter}/sub?target=${target}&url=${encodeURIComponent(url)}&insert=false&config=${encodeURIComponent(subConfig)}&emoji=true&list=false&tfo=false&scv=true&fdn=false&sort=false&new_name=true`;
}

function isClashCondition(userAgent, _url) {
    return (userAgent.includes('clash') && !userAgent.includes('nekobox')) || (_url.searchParams.has('clash') && !userAgent.includes('subConverter'));
}

function isSingboxCondition(userAgent, _url) {
    return userAgent.includes('sing-box') || userAgent.includes('singbox') || ((_url.searchParams.has('singbox') || _url.searchParams.has('sb')) && !userAgent.includes('subConverter'));
}

function splitNodeData(uniqueIpTxt, noTLS, host, uuid, userAgent, protType, nat64, hostRemark) {
    log(`splitNodeData----> \n host: ${host} \n uuid: ${uuid} \n protType: ${protType} \n hostRemark: ${hostRemark}`);

    const regionMap = {
        'SG': '🇸🇬 SG',
        'HK': '🇭🇰 HK',
        'KR': '🇰🇷 KR',
        'JP': '🇯🇵 JP',
        'GB': '🇬🇧 GB',
        'US': '🇺🇸 US',
        'TW': '🇼🇸 TW',
        'CF': '📶 CF'
    };
    function isLikelyHost(str) {
        if (!str) return false;
        str = str.trim();
        if (/\s|\/|\\|\(|\)|[\u4e00-\u9fff]/.test(str)) return false;
        if (/^(\d{1,3}\.){3}\d{1,3}(:\d+)?$/.test(str)) return true;
        if (/^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d+)?$/.test(str)) return true;
        return false;
    }

    const responseBody = uniqueIpTxt.map(raw => {
        const ipTxt = String(raw).trim();
        log(`splitNodeData---> ipTxt: ${ipTxt}`);
        let proxyip = "";
        let port = "443";
        let remarks = "";
        let address = "";

        const lastAt = ipTxt.lastIndexOf('@');
        let main = ipTxt;
        if (lastAt !== -1) {
            const candidate = ipTxt.slice(lastAt + 1).trim();
            if (isLikelyHost(candidate)) {
                proxyip = candidate;
                main = ipTxt.slice(0, lastAt);
                log(`splitNodeData--detected-proxy--> proxyip: ${proxyip}  main: ${main}`);
            } else {
                log(`splitNodeData--at-in-remark--> ignored candidate after @: ${candidate}`);
            }
        }

        const mainMatch = main.match(/^(\[.*\]|[^:#\s]+)(?::(\d+))?(?:#(.*))?$/);
        if (mainMatch) {
            address = mainMatch[1];
            port = mainMatch[2] || port;
            remarks = mainMatch[3] || "";
        } else {
            address = main;
            remarks = "";
        }

        if (hostRemark) {
            remarks = hostRemark;
        } else {
            remarks = (remarks && remarks.trim()) ? remarks.trim() : address;
        }

        const rmKey = String(remarks).trim().toUpperCase();
        if (regionMap[rmKey]) {
            remarks = regionMap[rmKey];
        }

        proxyip = proxyip || paddr;
        log(`splitNodeData--final--> \n address: ${address} \n port: ${port} \n remarks: ${remarks} \n proxyip: ${proxyip}`);

        if (noTLS !== 'true' && portSet_http.has(parseInt(port))) {
            return null;
        }

        const [v2, clash] = getConfigLink(uuid, host, address, port, remarks, proxyip, protType, nat64);
        return v2;
    }).filter(Boolean).join('\n');

    return responseBody;
}

async function getIpUrlTxtAndCsv(noTLS, urlTxts, urlCsvs, num) {
    if (noTLS === 'true') {
        return {
            txt: await getIpUrlTxt(urlTxts, num),
            csv: await getIpUrlCsv(urlCsvs, 'FALSE')
        };
    }
    return {
        txt: await getIpUrlTxt(urlTxts, num),
        csv: await getIpUrlCsv(urlCsvs, 'TRUE')
    };
}

async function getIpUrlTxt(urlTxts, num) {
    if (!urlTxts || urlTxts.length === 0) {
        return [];
    }

    let ipTxt = "";
    const controller = new AbortController();
    const timeout = setTimeout(() => {
        controller.abort();
    }, 2000);

    try {
        const urlMappings = urlTxts.map(entry => {
            const [url, suffix] = entry.split('@');
            return { url, suffix: suffix ? `@${suffix}` : '' };
        });

        const responses = await Promise.allSettled(
            urlMappings.map(({ url }) =>
                fetch(url, {
                    method: 'GET',
                    headers: {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;',
                        'User-Agent': projectName
                    },
                    signal: controller.signal
                }).then(response => response.ok ? response.text() : Promise.reject())
            )
        );

        for (let i = 0; i < responses.length; i++) {
            const response = responses[i];
            if (response.status === 'fulfilled') {
                const suffix = urlMappings[i].suffix;
                const content = response.value
                    .split('\n')
                    .filter(line => line.trim() !== "")
                    .map(line => line + suffix)
                    .join('\n');

                ipTxt += content + '\n';
            }
        }
    } catch (error) {
        errorLogs(error);
    } finally {
        clearTimeout(timeout);
    }
    log(`getIpUrlTxt-->ipTxt: ${ipTxt} \n `);
    let newIpTxt = await addIpText(ipTxt);
    const hasAcCom = urlTxts.includes(defaultIpUrlTxt);
    if (hasAcCom && typeof randomNum === 'number' && randomNum !== 0) {
        newIpTxt = getRandomItems(newIpTxt, num);
    }

    return newIpTxt;
}

async function getIpUrlTxtToArry(urlTxts) {
    if (!urlTxts || urlTxts.length === 0) {
        return [];
    }
    let ipTxt = "";
    const controller = new AbortController();

    const timeout = setTimeout(() => {
        controller.abort();
    }, 2000);

    try {
        const responses = await Promise.allSettled(urlTxts.map(apiUrl => fetch(apiUrl, {
            method: 'GET',
            headers: {
                'Accept': 'text/html,application/xhtml+xml,application/xml;',
                'User-Agent': projectName
            },
            signal: controller.signal
        }).then(response => response.ok ? response.text() : Promise.reject())));
        for (const response of responses) {
            if (response.status === 'fulfilled') {
                const content = await response.value;
                ipTxt += content + '\n';
            }
        }
    } catch (error) {
        errorLogs(error);
    } finally {
        clearTimeout(timeout);
    }

    const newIpTxt = await addIpText(ipTxt);
    log(`urlTxts: ${urlTxts} \n ipTxt: ${ipTxt} \n newIpTxt: ${newIpTxt} `);
    return newIpTxt;
}

async function getIpUrlCsv(urlCsvs, tls) {
    if (!urlCsvs || urlCsvs.length === 0) {
        return [];
    }
    const newAddressesCsv = [];

    const fetchCsvPromises = urlCsvs.map(async (csvUrl) => {
        const [url, suffix] = csvUrl.split('@');
        const suffixText = suffix ? `@${suffix}` : '';
        try {
            const response = await fetch(url);
            if (!response.ok) {
                errorLogs('Error fetching CSV:', response.status, response.statusText);
                return;
            }
            const text = await response.text();
            const lines = text.includes('\r\n') ? text.split('\r\n') : text.split('\n');
            if (lines.length < 2) {
                errorLogs('CSV file is empty or has no data rows');
                return;
            }
            const header = lines[0].trim().split(',');
            const tlsIndex = header.indexOf('TLS');
            const ipAddressIndex = 0;
            const portIndex = 1;
            const dataCenterIndex = tlsIndex + 1;
            const speedIndex = header.length - 1;
            if (tlsIndex === -1) {
                errorLogs('CSV file missing required TLS field');
                return;
            }

            for (let i = 1; i < lines.length; i++) {
                const columns = lines[i].trim().split(',');
                if (columns.length < header.length) {
                    continue;
                }
                const tlsValue = columns[tlsIndex].toUpperCase();
                const speedValue = parseFloat(columns[speedIndex]);
                if (tlsValue === tls && speedValue > sl) {
                    const ipAddress = columns[ipAddressIndex];
                    const port = columns[portIndex];
                    const dataCenter = columns[dataCenterIndex];
                    newAddressesCsv.push(`${ipAddress}:${port}#${dataCenter}${suffixText}`);
                }
            }
        } catch (error) {
            errorLogs('Error processing CSV URL:', csvUrl, error);
        }
    });

    await Promise.all(fetchCsvPromises);
    log(`newAddressesCsv: ${newAddressesCsv} \n `);
    return newAddressesCsv;
}

const meta = decodeBase64Utf8('PG1ldGEgbmFtZT0nZGVzY3JpcHRpb24nIGNoYXJzZXQ9J1VURi04JyBjb250ZW50PSdUaGlzIGlzIGEgcHJvamVjdCB0byBnZW5lcmF0ZSBmcmVlIHhodHRwL3ZsZXNzL3Ryb2phbiBub2Rlcy4gRm9yIG1vcmUgaW5mb3JtYXRpb24sIHBsZWFzZSBzdWJzY3JpYmUgeW91dHViZSjmlbDlrZflpZfliKkpIGh0dHBzOi8veW91dHViZS5jb20vQGFtX2NsdWJzIGFuZCBmb2xsb3cgR2l0SHViIGh0dHBzOi8vZ2l0aHViLmNvbS9hbWNsdWJzIGFuZCBmb2xsb3cgdGVsZWdyYW0gaHR0cHM6Ly90Lm1lL0FNX0NMVUJTICBhbmQgZm9sbG93ICBCbG9nIGh0dHBzOi8vYW1jbHVic3MuY29tJyAvPg==');
function getConfigHtml(host, remark, v2, clash) {
    log(`------------getConfigHtml------------------`);
    log(`id: ${id} \n host: ${host} \n remark: ${remark} \n v2: ${v2} \n clash: ${clash} `);
    const title = decodeBase64Utf8(fileName);
    const fullTitle = title + '-订阅器';

    const htmlHead = `
        <head>
        <title>${fullTitle}</title>
        ${meta}
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                color: #333;
                padding: 0;
                margin: 0;
                font-size: clamp(14px, 2.5vw, 18px);
            }
            a {
                text-decoration: none;
            }
            img {
                max-width: 100%;
                height: auto;
            }
            pre {
                white-space: pre-wrap;
                word-wrap: break-word;
                background-color: #fff;
                border: 1px solid #ddd;
                padding: 10px;
                border-radius: 8px;
                font-size: clamp(12px, 2.2vw, 16px);
            }
            .link-row {
                display: grid;
                grid-template-columns: 1fr 1fr; 
                gap: 14px 20px;                
                width: 100%;
                margin: 0 auto;
                padding: 0 0;                
                box-sizing: border-box;
            }
            .link-row a, button {
                display: block;
                width: 100%;
                text-align: center;
                padding: 12px 0;
                border-radius: 8px;
                font-weight: bold;
                cursor: pointer;
                border: none;
                transition: all 0.3s;
                background: linear-gradient(135deg, #5563DE, #3344cc);
                color: #fff;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                font-size: clamp(13px, 2.5vw, 16px);
            }
            .link-row a:hover, button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 12px rgba(0,0,0,0.2);
                background: linear-gradient(135deg, #3344cc, #223399);
            }
            @media (max-width: 600px) {
                .link-row {
                    grid-template-columns: 1fr 1fr; /* 仍两列 */
                    gap: 10px;
                }
                .link-row a, button {
                    font-size: 0.95rem;
                }
            }
            @media (max-width: 340px) {
                .link-row {
                    grid-template-columns: 1fr;
                }
            }
            @media (prefers-color-scheme: dark) {
                body {
                    background-color: #1e1e2f;
                    color: #f0f0f0;
                }
                pre {
                    background-color: #282a36;
                    border-color: #6272a4;
                }
            }
        </style>
        </head>
        `;

    const header = `
        <div class="links">
            <div class="link-row">
                <a href="${ytName}" target="_blank">🎬 YouTube</a>
                <a href="${tgName}" target="_blank">💬 Telegram</a>
                <a href="${ghName}" target="_blank">📂 GitHub</a>
                <a href="${bName}" target="_blank">🌐 Blog</a>
                <a href="https://${host}/${id}/ips" rel="noopener">⚡ 在线优选IP</a>
                <a href="https://${host}/${id}/setting" rel="noopener">⚙️ 自定义设置</a>
            </div>
        </div>
  `;

    const httpAddr = `https://${host}/${id}`;
    const output = cleanLines(`
        订阅地址支持 Base64、clash-meta、sing-box、Quantumult X、小火箭、surge 等订阅工具
        #########################################################
        通用订阅地址:${httpAddr}?sub<button onclick='copyToClipboard("${httpAddr}?sub")'><i class="fa fa-clipboard"></i>📋点击复制</button>
        #########################################################
        `);
    const output2 = cleanLines(`
        <div id="moreSection" style="display:none; margin-top:10px;">
            <pre>
            #########################################################
            clash订阅地址:${httpAddr}?clash<button onclick='copyToClipboard("${httpAddr}?clash")'><i class="fa fa-clipboard"></i>📋点击复制</button>
            #########################################################
            singbox订阅地址:${httpAddr}?singbox<button onclick='copyToClipboard("${httpAddr}?singbox")'><i class="fa fa-clipboard"></i>📋点击复制</button>
            #########################################################
            v2
            ${v2}
            #########################################################
            clash
            ${clash}
            #########################################################
            </pre>
        </div>
    `);
    const openSection = enableOpen ? `
        <pre>${output}</pre>
        <div style="text-align:center; margin-top:10px;">
            <button id="toggleBtn" onclick="toggleMore()">📂 展开查看更多</button>
        </div>
        ${output2}
    ` : '';

    const html = `
        <html>
        ${htmlHead}
        <body>
            ${header}
            ${openSection}
            <script>
                function copyToClipboard(text) {
                    navigator.clipboard.writeText(text)
                    .then(() => alert("Copied to clipboard"))
                    .catch(err => console.error("Failed to copy:", err));
                }

                function toggleMore() {
                    const section = document.getElementById("moreSection");
                    const btn = document.getElementById("toggleBtn");
                    if (section.style.display === "none") {
                        section.style.display = "block";
                        btn.textContent = "📁 收起内容";
                    } else {
                        section.style.display = "none";
                        btn.textContent = "📂 展开查看更多";
                    }
                }
            </script>

        </body>
        </html>
        `;
    return html;
}

function cleanLines(str) {
    return str
        .split('\n')
        .map(line => line.trimEnd())
        .map(line => line.replace(/^\s+/, ''))
        .filter((line, i, arr) => {
            if (i === 0 || i === arr.length - 1) {
                return line.trim() !== '';
            }
            return true;
        })
        .join('\n');
}


/** -------------------Home page-------------------------------- */
async function getSettingHtml(host) {
    const title = decodeBase64Utf8(fileName);
    const fullTitle = title + '-自定义设置';

    return `
    <html>
    <head>
    <title>${fullTitle}</title>
    ${meta}
    <style>
        :root {
            --primary: #5563DE;
            --primary-hover: #3344cc;
            --bg-light: linear-gradient(135deg, #f8faff, #eef1ff);
            --bg-dark: linear-gradient(135deg, #1e1e2f, #2a2a3f);
            --card-bg-light: #ffffff;
            --card-bg-dark: #2b2b3b;
            --text-light: #333;
            --text-dark: #f0f0f0;
            --border-light: #ddd;
            --border-dark: #444;
            --link-bg: #f0f0f0;
            --link-bg-dark: #3a3a4a;
            --link-color: #111;
        }

        body {
            font-family: "Segoe UI", Arial, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            background: var(--bg-light);
            color: var(--text-light);
            display: flex;
            justify-content: center;
            padding: 10px 0;
            transition: background 0.5s, color 0.5s;
        }

        @media (prefers-color-scheme: dark) {
            body {
                background: var(--bg-dark);
                color: var(--text-dark);
            }
        }

        .container {
            width: 90%;
            max-width: 650px;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .navbar-left {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: none;
            border: none;
            color: var(--primary);
            font-size: 14px;
            cursor: pointer;
            transition: color 0.3s, transform 0.2s;
        }

        .back-btn:hover {
            color: var(--primary-hover);
            transform: translateX(-2px);
        }

        .navbar-right a {
            margin-left: 12px;
            text-decoration: none;
            color: var(--primary);
            font-weight: 500;
            transition: color 0.3s;
            font-size: 14px;
        }

        .navbar-right a:hover {
            color: var(--primary-hover);
        }

        form {
            background: var(--card-bg-light);
            padding: 15px 15px;
            border-radius: 12px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.08);
            transition: background 0.5s, box-shadow 0.3s;
        }

        @media (prefers-color-scheme: dark) {
            form {
                background: var(--card-bg-dark);
                box-shadow: 0 6px 15px rgba(0,0,0,0.25);
            }
        }

        label {
            display: block;
            margin-top: 10px;
            font-weight: 600;
            font-size: 13px;
        }

        input, select {
            width: 100%;
            padding: 6px 8px;
            margin-top: 2px;
            border: 1px solid var(--border-light);
            border-radius: 6px;
            font-size: 13px;
            box-sizing: border-box;
            transition: border-color 0.3s, background 0.3s;
        }

        input:focus, select:focus {
            outline: none;
            border-color: var(--primary);
            background: #f9faff;
        }

        @media (prefers-color-scheme: dark) {
            input, select {
                background: #3a3a4a;
                border: 1px solid var(--border-dark);
                color: var(--text-dark);
            }
            input:focus, select:focus {
                background: #46465a;
            }
        }

        .form-title {
            text-align: center;
            font-size: 18px;
            font-weight: 600;
            color: var(--primary);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 4px;
        }

        .form-title .icon {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 24px;
            height: 24px;
            background: var(--primary);
            color: #fff;
            border-radius: 50%;
            font-size: 12px;
        }

        #generatedLink {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--link-bg);
            color: var(--link-color);
            font-size: 13px;
            padding: 4px 8px;
            border-radius: 6px;
            margin-bottom: 6px;
            word-break: break-all;
            }

        @media (prefers-color-scheme: dark) {
            #generatedLink {
                background: var(--link-bg-dark);
                color: #fff;
            }
        }

        #generatedLink button {
            background: var(--primary);
            color: #fff;
            border: none;
            padding: 2px 6px;
            font-size: 12px;
            border-radius: 4px;
            cursor: pointer;
        }

        #generatedLink button:hover {
            background: var(--primary-hover);
        }

        button.save-btn {
            width: 100%;
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.3s;
            margin-top: 4px;
        }

        button.save-btn:hover {
            background-color: var(--primary-hover);
            transform: translateY(-1px);
        }

        button.save-btn:active {
            transform: translateY(1px);
            }
            .error-msg {
            color: #e74c3c;
            font-size: 12px;
            margin-top: 2px;
            margin-bottom: 4px;
        }

    </style>
    </head>
    <body>
    <div class="container">
        <div class="navbar">
            <div class="navbar-left">
                <button class="back-btn" onclick="goHome()">🏠 返回主页</button>
            </div>
            <div class="navbar-right">
                <a href="https://youtube.com/@am_clubs?sub_confirmation=1" target="_blank">🎬 YouTube</a>
                <a href="https://t.me/am_clubs" target="_blank">💬 Telegram</a>
                <a href="https://github.com/am-cf-tunnel" target="_blank">📂 GitHub</a>
                <a href="https://amclubss.com" target="_blank">🌐 Blog</a>
            </div>
        </div>

        <form id="configForm">
        <h2 class="form-title"><span class="icon">⚙️</span> 自定义设置</h2>

        <div id="generatedLink" style="display:none;">
            <span id="linkText"></span>
            <button type="button" onclick="copyLink()">复制</button>
        </div>

        <label>UUID</label>
        <input type="text" id="UUID" name="HOUUIDST" placeholder="必填：UUID (例如：d0298536-d670-4045-bbb1-ddd5ea68683e)" />

        <label>HOST</label>
        <input type="text" id="HOST" name="HOST" placeholder="必填：Cloudflare节点域名 (例如：vless.amclubss.com)" />

        <label>IP_URL</label>
        <input type="text" id="IP_URL" name="IP_URL" placeholder="可选：优先IP地址 (例如：https://raw.github.../ipUrl.txt)" />

        <label>PROXYIP</label>
        <input type="text" id="PROXYIP" name="PROXYIP" placeholder="可选：反代IP或域名或地址 (例如：proxyip.amclubs.kozow.com)" />

        <label>SOCKS5</label>
        <input type="text" id="SOCKS5" name="SOCKS5" placeholder="可选：SOCKS5代理 (例如：socks5://user:pass@ip:port)" />

        <label>SUB_CONFIG</label>
        <input type="text" id="SUB_CONFIG" name="SUB_CONFIG" placeholder="可选：订阅转换配置文件 (例如：https://raw.github.../ACL4SSR_Online_Mini.ini)" />
        <label>SUB_CONVERTER</label>
        <input type="text" id="SUB_CONVERTER" name="SUB_CONVERTER" placeholder="可选：订阅转换后端api地址 (例如：url.v1.mk)" />

        <label>NAT64_PREFIX</label>
        <input type="text" id="NAT64_PREFIX" name="NAT64_PREFIX" placeholder="可选：NAT64前缀 (例如：2602:fc59:b0:64::)" />
        <label>NAT64</label>
        <select id="NAT64" name="NAT64">
            <option value="true">启用</option>
            <option value="false">关闭</option>
        </select>

        <label>PROT_TYPE</label>
        <select id="PROT_TYPE" name="PROT_TYPE">
            <option value="">默认</option>
            <option value="vless">vless</option>
            <option value="trojan">trojan</option>
        </select>

        <label>HOST_REMARK</label>
        <input type="text" id="HOST_REMARK" name="HOST_REMARK" placeholder="可选：默认是节点IP，所有节点别名" />

        <button type="button" class="save-btn" onclick="saveSettings()">💾 生成链接</button>
        </form>
    </div>

    <script>
        function goHome() {
            window.location.href = '/${id}';
        }

        function saveSettings() {
        const uuid = document.getElementById('UUID').value.trim();
        const hostInput = document.getElementById('HOST').value.trim();
        document.querySelectorAll('.error-msg').forEach(el => el.remove());
        let hasError = false;
        if (!uuid) {
            showError('UUID', '请填写 UUID');
            hasError = true;
        }
        if (!hostInput) {
            showError('HOST', '请填写 HOST');
            hasError = true;
        }
        if (hasError) return; 

        const params = new URLSearchParams();
        ['UUID','HOST','IP_URL','PROXYIP','SOCKS5','SUB_CONFIG','SUB_CONVERTER','HOST_REMARK','PROT_TYPE','NAT64','NAT64_PREFIX'].forEach(k => {
            const val = document.getElementById(k).value.trim();
            if (val) params.append(k, val);
        });

        const link = \`https://${host}/${id}?sub&\` + params.toString();
        const linkDiv = document.getElementById('generatedLink');
        const linkText = document.getElementById('linkText');
        linkText.textContent = link;
        linkDiv.style.display = 'flex';
        }

        function showError(fieldId, message) {
        const input = document.getElementById(fieldId);
        const error = document.createElement('div');
        error.className = 'error-msg';
        error.textContent = message;
        input.insertAdjacentElement('afterend', error);
        }

        function copyLink() {
        const linkText = document.getElementById('linkText').textContent;
        navigator.clipboard.writeText(linkText).then(() => {
            alert('链接已复制到剪贴板');
        });
        }
    </script>
    </body>
    </html>
    `;
}

async function login(req, env, res = null) {
    const method = req.method || (req instanceof Request ? req.method : 'GET');

    const renderLoginPage = (heading, status = 200) => {
        const html = renderPage({
            base64Title: pName,
            suffix: '-登录',
            heading,
            bodyContent: `
                <form method="POST">
                    <input type="password" name="password" placeholder="输入访问密码" required />
                    <button type="submit">登录</button>
                </form>
            `,
            ytName, tgName, ghName, bName
        });
        if (res && typeof res.setHeader === 'function') {
            res.setHeader("Content-Type", "text/html; charset=UTF-8");
            if (typeof res.status === 'function') {
                res.status(status).send(html);
            } else {
                res.write(html);
                res.end();
            }
            return;
        }
        return new Response(html, { status, headers: { "Content-Type": "text/html; charset=UTF-8" } });
    };

    log(`[LOGIN] → method: ${method}`);
    if (method === "GET") return renderLoginPage('🔐 请输入密码登录');

    if (method === "POST") {
        let body = '';
        if (req instanceof Request) {
            body = await req.text();
        } else if (req.on) {
            await new Promise(resolve => {
                req.on('data', chunk => { body += chunk.toString(); });
                req.on('end', resolve);
            });
        }

        const params = new URLSearchParams(body);
        const inputPassword = params.get("password")?.trim();
        log(`[LOGIN] → POST 输入密码: "${inputPassword}"`);

        if (inputPassword === id) {
            log(`[LOGIN] → 密码正确`);
            if (!uuid || !host) {
                return renderLoginPage(`❌ UUID或HOST变量未设置`, 400);
            }
            log(`[LOGIN] → 跳转到 id=${id}`);
            return redirectToId(id, req, res);
        } else {
            log(`[LOGIN] → 密码错误`);
            return renderLoginPage('❌ 密码错误，请重新尝试', 403);
        }
    }
    return renderLoginPage('Method Not Allowed', 405);
}

async function redirectToId(id, req, res = null) {
    if (!id) id = 'default';

    const envType = (typeof process !== 'undefined' && process.release?.name === 'node') ? 'Node/Vercel' :
        (typeof WebSocketPair !== 'undefined' && typeof addEventListener === 'function') ? 'Cloudflare Worker' :
            'Unknown';

    log(`[redirectToId] → id: ${id}, env: ${envType}, req.url: ${req.url}`);

    // Node / Vercel
    if (res) {
        log(`[redirectToId] → Node/Vercel 重定向到 /${id}`);
        res.writeHead(302, { Location: `/${id}` });
        res.end();
        return { status: 302, text: async () => '' }; // 返回对象，防止 mainHandler crash
    }

    // Edge / CF Worker
    const fullUrl = new URL(req.url, `https://${req.headers.get('host') || 'localhost'}`);
    log(`[redirectToId] → CF Worker 重定向到 ${fullUrl.origin}/${id}`);
    return Response.redirect(`${fullUrl.origin}/${id}`, 302);
}

function renderPage({ base64Title, suffix = '', heading, bodyContent, ytName, tgName, ghName, bName }) {
    const title = decodeBase64Utf8(base64Title);
    const fullTitle = title + suffix;

    return `<!DOCTYPE html>
    <html lang="zh-CN">
    <head>
    <meta charset="UTF-8">
    <title>${fullTitle}</title>
    <style>
    body {
        font-family: 'Segoe UI', Arial, sans-serif;
        background: linear-gradient(135deg, #5563de, #89f7fe);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        color: #333;
    }
    .login-container {
        background: #fff;
        padding: 35px 30px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        width: 380px;
        text-align: center;
        animation: fadeIn 0.6s ease-in-out;
    }
    h1 { font-size: 22px; margin-bottom: 20px; color: #444; }
    input[type="password"] {
        width: 100%;
        padding: 12px;
        font-size: 16px;
        margin-top: 10px;
        border: 1px solid #ccc;
        border-radius: 8px;
        box-sizing: border-box;
        text-align: center;
    }
    button {
        margin-top: 20px;
        width: 100%;
        padding: 12px;
        font-size: 16px;
        border: none;
        background-color: #5563de;
        color: white;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
        transition: background 0.3s;
    }
    button:hover { background-color: #3344cc; }
    .links { margin-top: 20px; font-size: 14px; }
    .link-row { display: flex; justify-content: space-between; margin-bottom: 10px; }
    .link-row a {
        flex: 1;
        margin: 0 5px;
        padding: 6px 0;
        color: #5563DE;
        text-decoration: none;
        text-align: center;
        border-radius: 6px;
        background: #f1f3ff;
        transition: all 0.3s;
    }
    .link-row a:hover { background: #e0e4ff; color: #333; }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @media (prefers-color-scheme: dark) {
        body {
            background: linear-gradient(135deg, #1e1e2f, #30324a);
            color: #f0f0f0;
        }
        .login-container { background: #2b2b3c; color: #eee; }
        input[type="password"] {
            background: #3a3a4d; color: #fff; border-color: #555;
        }
        button { background-color: #6b74e6; }
        .link-row a { background: #3a3a4d; color: #9db4ff; }
        .link-row a:hover { background: #4b4b6a; }
    }
    </style>
    </head>
    <body>
    <div class="login-container">
    <h1>${heading}</h1>
    ${bodyContent}
    <div class="links">
        <div class="link-row">
            <a href="${ytName}" target="_blank">🎬 YouTube</a>
            <a href="${tgName}" target="_blank">💬 Telegram</a>
        </div>
        <div class="link-row">
            <a href="${ghName}" target="_blank">📂 GitHub</a>
            <a href="${bName}" target="_blank">🌐 Blog</a>
        </div>
    </div>
    </div>
    </body>
    </html>`;
}


/** -------------------ips rtt-------------------------------- */
async function getNipHost(defaultHost) {
    const fallbackHost = base64Decode('NTUzNTU4Lnh5eg==');
    const rand = Math.random().toString(36).slice(2, 8);
    const sd = rand;
    const testUrl = `https://${sd}.${defaultHost}/cdn-cgi/trace?t=${Date.now()}`;
    async function fetchWithTimeout(url, timeout = 3000) {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), timeout);
        try {
            const res = await fetch(url, { method: 'HEAD', signal: controller.signal });
            return res;
        } finally {
            clearTimeout(timer);
        }
    }
    try {
        const res = await fetchWithTimeout(testUrl, 3000);
        if (res.ok) {
            log(`[NIP]: ${defaultHost} (${sd})`);
            return defaultHost;
        } else {
            log(`[NIP] returned ${res.status}, using fallback`);
            return fallbackHost;
        }
    } catch (err) {
        errorLogs(`[NIP] unreachable (${err.name}: ${err.message}), fallback to ${fallbackHost}`);
        return fallbackHost;
    }
}

async function fetchTextOrDefault(url, fallback = '') {
    try {
        const res = await fetch(url, { cf: { cacheEverything: true } });
        if (!res.ok) return fallback;
        return await res.text();
    } catch {
        return fallback;
    }
}

function ipToInt(ip) {
    return ip.split('.').reduce((acc, n) => (acc << 8) + parseInt(n, 10), 0) >>> 0;
}

function intToIp(int) {
    return [
        (int >>> 24) & 0xff,
        (int >>> 16) & 0xff,
        (int >>> 8) & 0xff,
        int & 0xff,
    ].join('.');
}

let basePadd = '\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0072\u0061\u0077\u002e\u0067\u0069\u0074\u0068\u0075\u0062\u0075\u0073\u0065\u0072\u0063\u006f\u006e\u0074\u0065\u006e\u0074\u002e\u0063\u006f\u006d\u002f\u0061\u006d\u0063\u006c\u0075\u0062\u0073\u002f\u0061\u006d\u002d\u0063\u0066\u002d\u0074\u0075\u006e\u006e\u0065\u006c\u002f\u006d\u0061\u0069\u006e\u002f\u0065\u0078\u0061\u006d\u0070\u006c\u0065\u002f\u0070\u0072\u006f\u0078\u0079\u0069\u0070\u005f\u0061\u006d\u002e\u0074\u0078\u0074';
async function loadIpSource(ipSource, targetPort) {
    async function fetchAsnPrefixes(asn) {
        log(`fetchAsnPrefixes-->asn: `, asn);
        const ipverseUrl = `\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0072\u0061\u0077\u002e\u0067\u0069\u0074\u0068\u0075\u0062\u0075\u0073\u0065\u0072\u0063\u006f\u006e\u0074\u0065\u006e\u0074\u002e\u0063\u006f\u006d\u002f\u0069\u0070\u0076\u0065\u0072\u0073\u0065\u002f\u0061\u0073\u006e\u002d\u0069\u0070\u002f\u006d\u0061\u0073\u0074\u0065\u0072\u002f\u0061\u0073\u002f${asn}\u002f\u0069\u0070\u0076\u0034\u002d\u0061\u0067\u0067\u0072\u0065\u0067\u0061\u0074\u0065\u0064\u002e\u0074\u0078\u0074`;
        let text = await fetchTextOrDefault(ipverseUrl, '');
        if (text && text.trim()) {
            log(`fetchAsnPrefixes-->fetchTextOrDefault: `, text.trim());
            return text.trim();
        }
        try {
            const apiUrl = `\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0061\u0070\u0069\u002e\u0062\u0067\u0070\u0076\u0069\u0065\u0077\u002e\u0069\u006f\u002f\u0061\u0073\u006e\u002f${asn}\u002f\u0070\u0072\u0065\u0066\u0069\u0078\u0065\u0073`;
            const resp = await fetch(apiUrl);
            if (!resp.ok) throw new Error('BGPView fetch failed');
            const data = await resp.json();
            if (data?.data?.ipv4_prefixes?.length) {
                log(`fetchAsnPrefixes-->bgpview: `, data.data.ipv4_prefixes.map(p => p.prefix).join('\n'));
                return data.data.ipv4_prefixes.map(p => p.prefix).join('\n');
            }
        } catch (e) {
            errorLogs(`Fallback BGPView failed for ASN ${asn}:`, e);
        }
        const defaultTxt = cleanLines(
            `173.245.48.0/20
            103.21.244.0/22
            103.22.200.0/22
            103.31.4.0/22
            141.101.64.0/18
            108.162.192.0/18
            190.93.240.0/20
            188.114.96.0/20
            197.234.240.0/22
            198.41.128.0/17
            162.158.0.0/15
            104.16.0.0/13
            104.24.0.0/14
            172.64.0.0/13
            131.0.72.0/22`);
        log(`fetchAsnPrefixes-->defaultTxt: `, defaultTxt);
        return defaultTxt;
    }

    function sampleFromCidrs(cidrInput, count = 1) {
        const cidrList = Array.isArray(cidrInput) ? cidrInput : cidrInput.split(/\r?\n/).map(line => line.trim()).filter(Boolean);
        const ipToInt = (ip) => ip.split('.').reduce((acc, octet) => (acc << 8) | Number(octet), 0) >>> 0;
        const intToIP = (int) => `${(int >>> 24) & 255}.${(int >>> 16) & 255}.${(int >>> 8) & 255}.${int & 255}`;
        const ranges = [];
        let totalWeight = 0;

        for (const cidr of cidrList) {
            if (!cidr.includes('/')) continue;
            const [network, prefixStr] = cidr.split('/');
            const prefix = Number(prefixStr);
            if (isNaN(prefix) || prefix < 0 || prefix > 32) continue;
            const networkInt = ipToInt(network);
            const hostBits = 32 - prefix;
            const numHosts = (1 << hostBits) - 2;
            if (numHosts <= 0) continue;
            ranges.push({ networkInt, numHosts });
            totalWeight += numHosts;
        }

        if (ranges.length === 0) return [];
        const sampled = new Set();

        while (sampled.size < count) {
            let pick = Math.random() * totalWeight;
            let chosenRange;
            for (const range of ranges) {
                pick -= range.numHosts;
                if (pick <= 0) {
                    chosenRange = range;
                    break;
                }
            }
            const offset = 1 + Math.floor(Math.random() * chosenRange.numHosts);
            sampled.add(intToIP(chosenRange.networkInt + offset));
            if (sampled.size >= totalWeight) break;
        }
        return Array.from(sampled);
    }

    if (ipSource === 'official') {
        const cfText = await fetchTextOrDefault('https://www.cloudflare.com/ips-v4/', '');
        return sampleFromCidrs(cfText, DEFAULT_TARGET_COUNT);
    }
    if (ipSource === 'proxyip' || ipSource === 'extraip' || ipSource === 'extraipProxy') {
        if (ipSource === 'extraip') {
            basePadd = extraIp;
        } else if (ipSource === 'extraipProxy') {
            basePadd = extraIpProxy;
        }
        const raw = await fetchTextOrDefault(basePadd, '');
        const validIps = raw.split('\n').map(l => l.trim()).filter(l => l && !l.startsWith('#'))
            .map(l => {
                const m = l.match(/(\d+\.\d+\.\d+\.\d+)/);
                return m ? m[1] : null;
            }).filter(Boolean);
        if (validIps.length > DEFAULT_TARGET_COUNT) {
            const shuffled = validIps.sort(() => 0.5 - Math.random());
            return shuffled.slice(0, DEFAULT_TARGET_COUNT);
        }
        return validIps;
    }
    const cidrText = await fetchAsnPrefixes(ipSource);
    return sampleFromCidrs(cidrText, DEFAULT_TARGET_COUNT);
}

/** -------------------ips rtt kv-------------------------------- */
async function cfKvRestPut(env, key, value) {
    const namespaceId = getEnvVar("CF_NAMESPACE_ID", env);
    const accountId = getEnvVar("CF_ACCOUNT_ID", env);
    const email = getEnvVar("CF_EMAIL", env);
    const apiKey = getEnvVar("CF_API_KEY", env);
    const url = `https://api.cloudflare.com/client/v4/accounts/${accountId}/storage/kv/namespaces/${namespaceId}/values/${encodeURIComponent(key)}`;

    const res = await fetch(url, {
        method: "PUT",
        headers: {
            "X-Auth-Email": email,
            "X-Auth-Key": apiKey,
            "Content-Type": "text/plain"
        },
        body: value
    });
    const data = await res.json();
    if (!data.success) {
        throw new Error(JSON.stringify(data));
    }
}

async function cfKvRestGet(env, key) {
    const namespaceId = getEnvVar("CF_NAMESPACE_ID", env);
    const accountId = getEnvVar("CF_ACCOUNT_ID", env);
    const email = getEnvVar("CF_EMAIL", env);
    const apiKey = getEnvVar("CF_API_KEY", env);
    const url = `https://api.cloudflare.com/client/v4/accounts/${accountId}/storage/kv/namespaces/${namespaceId}/values/${encodeURIComponent(key)}`;

    const res = await fetch(url, {
        method: "GET",
        headers: {
            "X-Auth-Email": email,
            "X-Auth-Key": apiKey
        }
    });
    if (res.status === 404) return null;
    return await res.text();
}

async function saveToKV(env, key, value) {
    if (isCloudflareRuntime(env)) {
        if (!env.ips || typeof env.ips.put !== "function") {
            throw new Error("Cloudflare KV binding 'ips' not found");
        }
        await env.ips.put(key, value);
    } else {
        await cfKvRestPut(env, key, value);
    }
}

async function loadFromKV(env, key) {
    try {
        if (isCloudflareRuntime(env)) {
            if (!env.ips || typeof env.ips.get !== "function") {
                return null;
            }
            return await env.ips.get(key);
        }
        return await cfKvRestGet(env, key);
    } catch (e) {
        return null;
    }
}

async function appendToKV(env, key, appendText) {
    const existing = await loadFromKV(env, key);
    const existingArr = existing ? existing.split('\n').map(v => v.trim()).filter(v => v) : [];
    const appendArr = appendText.split('\n').map(v => v.trim()).filter(v => v);
    const mergedArr = Array.from(new Set([...existingArr, ...appendArr]));
    const merged = mergedArr.join('\n');
    return await saveToKV(env, key, merged);
}

/** -------------------ips rtt html-------------------------------- */
function htmlPage() {
    const title = decodeBase64Utf8(fileName);
    const fullTitle = title + '-在线优选IP';

    return `<!doctype html>
    <html lang="zh-CN">
    <head>
    <title>${fullTitle}</title>
    ${meta}
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <title>Cloudflare IP 优选延迟测试</title>
    <style>
    :root {
        --bg-color: #0d1117;
        --panel-bg: #161b22;
        --text-color: #e6edf3;
        --accent: #58a6ff;
        --success: #2ea043;
        --danger: #f85149;
        --border: #30363d;
    }

    body {
        margin: 0;
        font-family: system-ui, Segoe UI, Roboto, Arial;
        background: radial-gradient(circle at top left, #0d1117, #0b0e14);
        color: var(--text-color);
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }

    .header {
        width: 100%;
        max-width: 1200px;
        padding: 14px 24px;
        margin-bottom: 24px;
        background: linear-gradient(90deg, #0d1117, #1b222d);
        border: 1px solid var(--border);
        border-radius: 14px;
        font-size: 22px;
        font-weight: 600;
        color: var(--accent);
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.4);
        box-sizing: border-box;
        margin-left: auto; 
        margin-right: auto;
        text-align: center;
        line-height: 1.6;
        letter-spacing: 0.5px;
    }

    .section {
        padding: 0 12px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        width: 100%;
        max-width: 1200px;
        margin-bottom: 20px;
    }

    .panel {
        background: var(--panel-bg);
        border-radius: 14px;
        border: 1px solid var(--border);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
        padding: 16px 20px;
        flex: 1;
        width: 100%;          
        box-sizing: border-box; 
        max-width: 580px;
    }

    .panel:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
    }

    .sameHeight {
        min-height: 240px;
    }

    /* 表单 */
    label, select, input, button {
        font-size: 14px;
        margin: 4px;
        padding: 8px 6px;
        border-radius: 6px;
    }

    select, input {
        border: 1px solid var(--border);
        background: #0d1117;
        color: var(--text-color);
    }

    button {
        border: none;
        background: var(--accent);
        color: #fff;
        cursor: pointer;
        transition: 0.2s;
        box-shadow: 0 1px 4px rgba(88, 166, 255, 0.3);
    }

    button:hover {
        background: #1f6feb;
        box-shadow: 0 2px 8px rgba(88, 166, 255, 0.4);
    }

    button:disabled {
        background: #555;
        color: #aaa;
        cursor: not-allowed;
        box-shadow: none;
    }

    /* 表格 */
    .resultTableWrapper {
        max-height: 200px;
        overflow-y: auto;
        display: block;
    }

    .resultTableWrapper table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        padding: 8px;
        border-bottom: 1px solid var(--border);
        text-align: left;
    }

    thead th {
        position: sticky;
        top: 0;
        background: #1b212c;
        z-index: 1;
    }

    tbody tr:nth-child(even) {
        background: rgba(255, 255, 255, 0.03);
    }

    tbody tr:hover {
        background: rgba(88, 166, 255, 0.1);
    }

    /* 进度条 */
    #progressBar, #proxyProgressBar {
        width: 100%;
        height: 12px;
        background: #30363d;
        border-radius: 8px;
        overflow: hidden;
        margin-top: 8px;
    }

    .progressFill {
        height: 100%;
        width: 0;
        background: linear-gradient(90deg, var(--success), #3fb950);
        transition: width 0.25s ease;
    }

    #proxyProgressText, #progressBarText{
        margin-top: 4px;
        font-size: 13px;
        color: #fff; 
        text-align: center;
        font-weight: 500;
    }

    /* 日志 */
    #logPanel {
        width: 100%;
        max-width: 1200px;
        background: var(--panel-bg);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
    }

    #clearLog {
        float: right;
        background: var(--danger);
    }

    #clearLog:hover {
        background: #da3633;
    }

    pre {
        background: #0d1117;
        border-radius: 6px;
        padding: 10px;
        overflow: auto;
        max-height: 300px;
        font-size: 13px;
        line-height: 1.4;
    }

    /* 响应式 */
    @media (max-width: 768px) {
        .section {
            flex-direction: column;
            align-items: stretch;
        }
        .panel {
            width: 100%;
            max-width: 100%;
        }
        button, input, select {
            width: calc(100% - 12px);
        }
        .navbar {
            justify-content: flex-start;
            gap: 6px;
        }
        .navbar-right a,
        .back-btn {
            font-size: 13px;
            padding: 4px 6px;
            color: #fff;
        }
    }

    .back-btn {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: none;
        border: none;
        color: var(--primary);
        font-size: 14px;
        cursor: pointer;
        transition: color 0.3s, transform 0.2s;
        white-space: nowrap; 
        padding: 6px 10px; 
    }
    .back-btn:hover {
        color: var(--primary-hover);
        transform: translateX(-2px);
    }
    .navbar {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-bottom: 5px;
        overflow-x: auto;  
        white-space: nowrap;
        gap: 8px;    
        padding-bottom: 4px; 
    }
    .navbar::-webkit-scrollbar {
        display: none;  
    }
    .navbar-left,
    .navbar-right {
        display: flex;
        align-items: center;
        gap: 6px;
        color: #fff;
    }
    .navbar-right a {
        margin-left: 5px;
        text-decoration: none;
        color: #fff;  
        font-weight: 500;
        transition: color 0.3s;
        font-size: 14px;
    }
    .navbar-right a:hover {
        color: #fff;
        opacity: 0.8; 
    }
  </style>
  </head>
  <body>
    <div class="navbar">
        <div class="navbar-left">
            <button class="back-btn" onclick="goHome()">🏠 主页</button>
        </div>
        <div class="navbar-right">
            <a href="https://youtube.com/@am_clubs?sub_confirmation=1" target="_blank">🎬 YouTube</a>
            <a href="https://t.me/am_clubs" target="_blank">💬 Telegram</a>
            <a href="https://github.com/am-cf-tunnel" target="_blank">📂 GitHub</a>
            <a href="https://amclubss.com" target="_blank">🌐 Blog</a>
        </div>
    </div>
    <span id="cf-check" style="font-size:0.9em;"></span>
    <div class="header">☁️ Cloudflare IP 优选工具</div>
    <!-- 第一组 -->
    <div class="section">
      <div class="panel sameHeight">
        <h3>⚙️ Cloudflare在线优选IP</h3>
        <div>
          <label>IP 源：
            <select id="ipSource">
              <option value="official">Cloudflare官方</option>
              <option value="13335">AS13335(CF)</option>
              <option value="209242">AS209242(CF London)</option>
              <option value="24429">AS24429(阿里云)</option>
              <option value="35916">AS35916(MULTACOM)</option>
              <option value="199524">AS199524(G-Core)</option>
            </select>
          </label>
          <label>端口：
            <select id="targetPort">
              <option value="443">443</option>
              <option value="8443">8443</option>
              <option value="2053">2053</option>
              <option value="2096">2096</option>
              <option value="2087">2087</option>
              <option value="2083">2083</option>
            </select>
          </label>
          <!-- <label>并发：<input id="concurrency" value="20" size="3"></label>-->
        </div>
        <div>
          <button id="testBtnNormal" >🚀 开始测试</button>
          <button id="cancelBtnNormal" disabled>⏹️ 取消测试</button>
          <button id="saveBtnNormal" disabled>💾 覆盖保存</button>
          <button id="appendBtnNormal" disabled>📥 追加保存</button>
          <button id="copyBtnNormal" disabled>📋 复制结果</button>
          <!-- <button id="loadBtnNormal">📂 导出文件</button> -->
        </div>
        <div id="progressBar"><div id="progressFill" class="progressFill"></div></div>
        <div id="progressBarText">尚未开始测试</div>
        <div id="saveStatus" style="font-size:12px;color:#999;margin-top:10px;">
          HKG=中国香港, TPE=中国台湾, SJC=美国圣何塞, LAX=美国洛杉矶, SEA=美国西雅图,
          NRT=日本东京, SIN=新加坡, KIX=日本大阪, FRA=德国法兰克福, LHR=英国伦敦, SYD=澳大利亚悉尼
        </div>
      </div>

      <div class="panel sameHeight">
        <h3>📊 Cloudflare在线优选IP 结果</h3>
        <div id="resultSummary">尚未测试</div>
        <div class="resultTableWrapper" id="resultWrapper">
          <table>
            <thead><tr><th>#</th><th>IP</th><th>RTT(ms)</th><th>COLO</th></tr></thead>
            <tbody id="resultTable"></tbody>
          </table>
        </div>
      </div>
      
    </div>

    <!-- 第二组 -->
    <div class="section">
      <div class="panel sameHeight">
        <h3>🌐 Cloudflare在线优选反代IP</h3>
        <div>
          <label>反代IP源：
            <select id="proxySource">
              <option value="proxyip">proxyip(AM优选)</option>
              <option value="36352">AS36352(美国)</option>
              <option value="25820">AS25820(美国)</option>
              <option value="25693">AS25693(美国)</option>
              <option value="142132">AS142132(新加坡)</option>
              <option value="51290">AS51290(英国)</option>
              <option value="209847">AS209847(土耳其)</option>
            </select>
          </label>
          <label>端口：
            <select id="proxyTargetPort">
              <option value="443">443</option>
              <option value="8443">8443</option>
              <option value="2053">2053</option>
              <option value="2096">2096</option>
              <option value="2087">2087</option>
              <option value="2083">2083</option>
            </select>
          </label>
          <!-- <label>并发：<input id="proxyConcurrency" value="20" size="3"></label>-->
        </div>
        <div>
          <button id="testBtnProxy" >🚀 开始测试</button>
          <button id="cancelBtnProxy" disabled>⏹️ 取消测试</button>
          <button id="saveBtnProxy" disabled>💾 覆盖保存</button>
          <button id="appendBtnProxy" disabled>📥 追加保存</button>
          <button id="copyBtnProxy" disabled>📋 复制结果</button>
          <!-- <button id="loadBtnProxy">📂 导出文件</button> -->
        </div>
        <div id="proxyProgressBar"><div id="proxyProgressFill" class="progressFill"></div></div>
        <div id="proxyProgressText">尚未开始测试</div>
        <div id="saveStatusProxy" style="font-size:12px;color:#999;margin-top:10px;">
          HKG=中国香港, TPE=中国台湾, SJC=美国圣何塞, LAX=美国洛杉矶, SEA=美国西雅图,
          NRT=日本东京, SIN=新加坡, KIX=日本大阪, FRA=德国法兰克福, LHR=英国伦敦, SYD=澳大利亚悉尼
        </div>
      </div>

      <div class="panel sameHeight">
        <h3>📊 Cloudflare在线优选反代IP 结果</h3>
        <div id="proxyResultSummary">尚未测试</div>
        <div class="resultTableWrapper" id="proxyResultWrapper">
          <table>
            <thead><tr><th>#</th><th>IP</th><th>RTT(ms)</th><th>COLO</th></tr></thead>
            <tbody id="proxyResultTable"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 日志 
    <div class="panel" id="logPanel">
      <h3>🧾 测试日志 <button id="clearLog">🧹 清空日志</button></h3>
      <pre id="log"></pre>
    </div>
    -->

    <script>${pageLogic()}</script>
  </body>
  </html>`;
}

function pageLogic() {
    return `
    const extraValue = "${extraIp || ''}";
    if (extraValue) {
        const select = document.getElementById("ipSource");
        const option = document.createElement("option");
        option.value = 'extraip';
        option.textContent = '自定义源';
        select.appendChild(option);
    }

    const extraValueProxy = "${extraIpProxy || ''}";
    if (extraValueProxy) {
        const selectProxy = document.getElementById("proxySource");
        const optionProxy = document.createElement("option");
        optionProxy.value = 'extraipProxy';
        optionProxy.textContent = '自定义反代源';
        selectProxy.appendChild(optionProxy);
    }

    let cancelRequested = false;
    //✅ 存所有未完成请求
    let activeControllers = []; 
    //✅ 页面加载完毕后绑定事件
    window.addEventListener('DOMContentLoaded', () => {
      document.getElementById('testBtnNormal').addEventListener('click', startTest);
      document.getElementById('testBtnProxy').addEventListener('click', startTest);
      document.getElementById('cancelBtnNormal').addEventListener('click', cancelTest);
      document.getElementById('cancelBtnProxy').addEventListener('click', cancelTest);
      // document.getElementById('clearLog').addEventListener('click', () => {
      //   document.getElementById('log').textContent = '';
      // });
      document.getElementById('copyBtnNormal').addEventListener('click', () => copyTop50(false));
      document.getElementById('copyBtnProxy').addEventListener('click', () => copyTop50(true));
      document.getElementById('saveBtnNormal').addEventListener('click', () => saveTop50(false));
      document.getElementById('saveBtnProxy').addEventListener('click', () => saveTop50(true));
      document.getElementById('appendBtnNormal').addEventListener('click', () => appendTop50(false));
      document.getElementById('appendBtnProxy').addEventListener('click', () => appendTop50(true));
    });
    // -----------------------------------------------------------------------------//
    async function startTest(event) {
      const btn = event.target;
      const isProxy = btn.id === 'testBtnProxy';
      const ipSourceSelect = document.getElementById(isProxy ? 'proxySource' : 'ipSource');
      const portSelect = document.querySelector(isProxy ? '#proxyTargetPort:last-of-type' : '#targetPort:first-of-type');
      const concurrencyInput = document.getElementById(isProxy ? 'proxyConcurrency' : 'concurrency');
      const progressFill = document.getElementById(isProxy ? 'proxyProgressFill' : 'progressFill');
      const progressText = document.getElementById(isProxy ? 'proxyProgressText' : 'progressBarText');
      const resultTable = document.getElementById(isProxy ? 'proxyResultTable' : 'resultTable');
      const resultSummary = document.getElementById(isProxy ? 'proxyResultSummary' : 'resultSummary');
      const cancelBtn = document.getElementById(isProxy ? 'cancelBtnProxy' : 'cancelBtnNormal');
      const copyBtn = document.getElementById(isProxy ? 'copyBtnProxy' : 'copyBtnNormal');
      const saveBtn = document.getElementById(isProxy ? 'saveBtnProxy' : 'saveBtnNormal');
      const appendBtn = document.getElementById(isProxy ? 'appendBtnProxy' : 'appendBtnNormal');
      
      const selectedPort = portSelect.value;
      const selectedIPSource = ipSourceSelect.value;
      const ipSourceName = ipSourceSelect.options[ipSourceSelect.selectedIndex].text;

      cancelBtn.disabled = false;
      cancelRequested = false;
      activeControllers = [];
      btn.disabled = true;
      btn.textContent = '加载IP列表...';
      portSelect.disabled = true;
      ipSourceSelect.disabled = true;
      testResults = [];
      displayedResults = []; 
      showingAll = false; 
      currentDisplayType = 'loading';

      //✅ 重置
      progressFill.style.width = '0%';
      resultSummary.textContent = '正在加载 ' + ipSourceName + ' IP列表...';
      const tableBody = resultTable;
      tableBody.innerHTML = '';
      progressText.textContent = '开始加载IP列表中...';
      
      //✅ 获取IP列表
      const originalIPs = await ipsFetch(selectedIPSource, selectedPort);
      if (!originalIPs || originalIPs.length === 0) {
        btn.disabled = false;
        btn.textContent = '开始延迟测试';
        portSelect.disabled = false;
        ipSourceSelect.disabled = false;
        resultSummary.textContent = '加载IP列表失败，请重试';
        return;
      }
      //✅ 显示加载到的IP列表（右侧表格）
      tableBody.innerHTML = ''; 
      const ips = Array.isArray(originalIPs) ? originalIPs : originalIPs.split('\\n');
      ips.forEach((ip, i) => {
        const row = document.createElement('tr');
        row.innerHTML = '<td>' + (i + 1) + '</td><td>' + ip + '</td><td>-</td><td>-</td>';
        tableBody.appendChild(row);
      });
      resultSummary.textContent = '已加载 ips.length  个 IP，准备开始测试...';
        
      //✅ 开始测试
      btn.textContent = '测试中...';
      resultSummary.textContent = '开始测试端口 ' + selectedPort + '...';
      currentDisplayType = 'testing';
      progressText.textContent = '开始测试中...';
      const results = await ipBatchTest(progressFill,progressText,tableBody, ips, selectedPort, 32);
      //testResults = results.sort((a, b) => a.latency - b.latency);
      
      //✅ 显示结果
      copyBtn.disabled = false;
      saveBtn.disabled = false;
      appendBtn.disabled = false;
      currentDisplayType = 'results'; 
      showingAll = false;
      cancelBtn.disabled = true; 
      btn.disabled = false;
      btn.textContent = '重新测试';
      portSelect.disabled = false;
      ipSourceSelect.disabled = false;
      testResults = results;
      const text = ' - 有效IP: ' + testResults.length + '/' + originalIPs.length + ' (端口: ' + selectedPort + ', IP库: ' + ipSourceName + ')';
      resultSummary.textContent = cancelRequested? '已取消' + text : '已完成'  + text;
    }

    // ✅ 批量扫描 + 最大并发控制 + 有序输出 + 可取消
    async function ipBatchTest(progressFill, progressText, tableBody, ips, port, maxConcurrent = 32) {
      const total = ips.length;
      const results = new Array(total).fill(null);
      let completed = 0;
      let tested = 0;
      let index = 0;
      tableBody.innerHTML = '';

      async function worker() {
        while (!cancelRequested) {
          const currentIndex = index++;
          if (currentIndex >= total) break;
          const ip = ips[currentIndex];
          const res = await testIP(ip, port);
          if (cancelRequested) return;
          if (res) {
            results[currentIndex] = res;
            insertSortedRow(tableBody, res);
          }
          completed++;
          const percent = ((completed / total) * 100).toFixed(1);
          const valid = results.filter(Boolean).length;
          progressText.textContent = \`测试中: \${ ip } | 完成 \${ completed }/\${total} | 有效 \${valid} (\${percent}%)\`;
          progressFill.style.width = percent + '%';
          if (completed % 6 === 0) await new Promise(r => setTimeout(r, 0));
        }
      }

      const workers = Array(Math.min(maxConcurrent, total)) .fill().map(() => worker());
      await Promise.all(workers);

      if (cancelRequested) {
          progressText.textContent = \`⏹️ 已取消测试（有效IP \${valid}/\${total}）\`;
          return results.filter(Boolean).sort((a, b) => a.latency - b.latency);
      }

      const valid = results.filter(Boolean).length;
      progressFill.style.width = '100%';
      progressText.textContent = \`✅ 测试完成!(有效IP \${valid}/\${total}) \`;
      const filtered = results.filter(Boolean).sort((a, b) => a.latency - b.latency);
      return filtered;
    }

    // ✅ 更安全且更快的请求 + 超时封装
    function fetchWithTimeout(url, timeout) {
      const controller = new AbortController();
      activeControllers.push(controller);
      const timer = setTimeout(() => controller.abort(), timeout);
      return fetch(url, { signal: controller.signal, mode: 'cors' })
        .finally(() => {
          clearTimeout(timer);
          activeControllers = activeControllers.filter(c => c !== controller);
        }).catch(err => null);
    }

    // ✅ 单个 IP 测试
    async function runTest(ip, port, timeout) {
      if (cancelRequested) return null;
      const nip = ip.split('.') .map(n => Number(n).toString(16).padStart(2, '0')).join('');
      const url = 'https://' + nip + '.${nipHost}:' + port + '/cdn-cgi/trace?t=${Date.now()}';
      const start = Date.now();
      const res = await fetchWithTimeout(url, timeout);
      if (!res || res.status !== 200) return null;

      const text = await res.text();
      const trace = buildTrace(text);
      if (!trace?.colo || !trace?.ip) return null;
      const latency = Date.now() - start;
      return {
        ip,
        port,
        latency,
        colo: trace.colo,
        responseIP: trace.ip,
        type: trace.ip.includes(':') || trace.ip === ip ? 'proxy' : 'official'
      };
    }

    // ✅ 自动重试 3 次
    async function testIP(ip, port, timeout = 5000) {
        let lastFail = null;
        for (let tryCount = 1; tryCount <= 3; tryCount++) {
            if (cancelRequested) return null;
            const result = await runTest(ip, port, timeout);
            if (result) return result;
            lastFail = result;
            await new Promise(r => setTimeout(r, 150));
        }
        return null;
    }

    // ✅ 提取 trace 信息
    function buildTrace(text) {
        const obj = {};
        text.trim().split('\\n').forEach(line => {
            const [k, v] = line.split('=');
            if (k && v) obj[k.trim()] = v.trim();
        });
        return obj;
    }

    //✅ 获取IP列表
    async function ipsFetch(ipSource, port) {
        try {
            const response = await fetch(\`/ipsFetch?ipSource=\${ipSource}&port=\${port}\`, { method: 'GET'});
            if (!response.ok) {
                throw new Error('Failed to load IPs');
            }
            const data = await response.json();
            return data.ips || [];
        } catch (error) {
            console.error('加载IP列表失败:', error);
            return [];
        }
    }

    //✅ 显示优先列表
    function insertSortedRow(tableBody, res) {
      if (cancelRequested) return;
      const rows = tableBody.rows;
      let insertIndex = rows.length;
      for (let i = 0; i < rows.length; i++) {
        const existingLatency = parseInt(rows[i].cells[2].textContent);
        if (res.latency < existingLatency) {
          insertIndex = i;
          break;
        }
      }
      const row = tableBody.insertRow(insertIndex);
      row.insertCell().textContent = insertIndex + 1;
      row.insertCell().textContent = res.ip;
      row.insertCell().textContent = \`\${ res.latency } ms\`;
      row.insertCell().textContent = res.colo || 'CF优选';
      for (let i = 0; i < tableBody.rows.length; i++) {
        tableBody.rows[i].cells[0].textContent = i + 1;
      }
      for (let i = 0; i < tableBody.rows.length; i++) {
        if (i === 0) {
          tableBody.rows[i].style.background = "rgba(46,160,67,0.2)";
        } else {
          tableBody.rows[i].style.background = "";
        }
      }
    }

    //✅ 取消操作
    function cancelTest(event) {
      cancelRequested = true;
      activeControllers.forEach(c => {
        try { c.abort(); } catch {}
      });
      activeControllers = [];
      const isProxy = event.target.id === 'cancelBtnProxy';
      const progressText = document.getElementById(isProxy ? 'proxyProgressText' : 'progressBarText');
      progressText.textContent = '⏹ 已取消测试';
      const tableBody = document.getElementById(isProxy ? 'proxyResultTable' : 'resultTable');
      currentDisplayType = 'cancelled';
      const testBtn = document.getElementById(isProxy ? 'testBtnProxy' : 'testBtnNormal');
      testBtn.disabled = false;
      testBtn.textContent = "重新测试";
      event.target.disabled = true;
    }
     
    //✅ 复制操作
    function copyTop50(isProxy) {
      const resultTable = document.getElementById(isProxy ? 'proxyResultTable' : 'resultTable');
      const port = document.getElementById(isProxy ? 'proxyTargetPort' : 'targetPort').value;
      const rows = Array.from(resultTable.rows).slice(0, 50);
      if (rows.length === 0) {
        alert("没有可复制的结果");
        return;
      }
      const lines = rows.map(row => {
        const ip = row.cells[1].textContent;
        const colo = row.cells[3].textContent;
        return \`\${ ip }:\${ port }#\${ colo }\`;
      });
      const textToCopy = lines.join('\\n');
      navigator.clipboard.writeText(textToCopy)
        .then(() => alert("✅ 已复制前 50 个优选IP"))
        .catch(() => alert("❌ 复制失败，请手动复制"));
    }

    //✅ KV保存操作
    function saveTop50(isProxy) {
      const resultTable = document.getElementById(isProxy ? 'proxyResultTable' : 'resultTable');
      const port = document.getElementById(isProxy ? 'proxyTargetPort' : 'targetPort').value;
      const saveStatus = document.getElementById(isProxy ? 'saveStatusProxy' : 'saveStatus');
      const rows = Array.from(resultTable.rows).slice(0, 50);
      if (rows.length === 0) {
        saveStatus.style.color = '#f85149';
        saveStatus.textContent = '⚠ 没有可保存的结果';
        return;
      }
      const lines = rows.map(row => {
        const ip = row.cells[1].textContent;
        const colo = row.cells[3].textContent;
        return \`\${ ip }:\${ port }#\${ colo } \`;
      });
      const textToSave = lines.join("\\n");
      const key = \`cf_\${ isProxy ? "proxy" : "normal" }_ip\`;

      fetch('/${id}/save', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          key,
          items: textToSave
        })
      })
      .then(res => res.json())
      .then(r => {
        if (r.ok) {
          saveStatus.style.color = '#2ea043'; 
          saveStatus.textContent = \`✅ 覆盖保存成功，共 \${ lines.length } 条\`;
        } else {
          saveStatus.style.color = '#f85149';
          saveStatus.textContent = \`❌ 保存失败：\${ r.error || "未知错误" } \`;
        }
      })
      .catch(err => {
        saveStatus.style.color = '#f85149';
        saveStatus.textContent = \`❌ 保存异常：\${ err.message }\`;
      });
    }

    //✅ KV追加操作
    async function appendTop50(isProxy) {
      const resultTable = document.getElementById(isProxy ? 'proxyResultTable' : 'resultTable');
      const port = document.getElementById(isProxy ? 'proxyTargetPort' : 'targetPort').value;
      const saveStatus = document.getElementById(isProxy ? 'saveStatusProxy' : 'saveStatus');
      const rows = Array.from(resultTable.rows).slice(0, 50);
      if (rows.length === 0) {
        saveStatus.style.color = '#f85149';
        saveStatus.textContent = "⚠ 没有可追加的数据";
        return;
      }
      const lines = rows.map(row => {
        const ip = row.cells[1].textContent.trim();
        const colo = row.cells[3].textContent.trim();
        return \`\${ip}:\${ port }#\${colo}\`;
      });
      const key = \`cf_\${ isProxy ? "proxy" : "normal" }_ip\`;
      try {
        const saveResp = await fetch('/${id}/append', {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ key, items: lines.join('\\n') })
        });
        const result = await saveResp.json();
        if (result.ok) {
          saveStatus.style.color = '#2ea043';
          saveStatus.textContent = \`✅ 已追加并保存成功，共 \${ lines.length } 条\`;
        } else {
          saveStatus.style.color = '#f85149';
          saveStatus.textContent = \`❌ 保存失败：\${ result.error || "未知错误" } \`;
        }
      } catch (error) {
        saveStatus.style.color = '#f85149';
        saveStatus.textContent = \`❌ 保存异常：\${ error.message } \`;
      }
    }

    function goHome() {
        window.location.href = '/${id}';
    }

     //🌐
    async function detectProxyOrVPN() {
        const container = document.querySelector("#cf-check") || document.body;
        const notice = document.createElement("div");
        notice.style.marginTop = "8px";
        notice.style.fontSize = "0.95em";
        container.appendChild(notice);

        try {
            const cfRes = await fetch("https://speed.cloudflare.com/cdn-cgi/trace?t=${Date.now()}");
            const cfText = await cfRes.text();

            const text = cfText.trim().split("\\n");
            const data = {};
            text.forEach(line => {
                const [key, value] = line.split('=');
                if (key && value) data[key.trim()] = value.trim();
            });
            const ip = data.ip || '未知';
            const loc = data.loc || '未知';

            let message = \`✅ 您当前检测为CN地区网络，可以进行优选\`;
            let color = "limegreen";
            // loc=CN 不一致 → 代理或 VPN
            if (loc !== 'CN') {
                message = \`⚠️您当前使用了 <b>代理或VPN</b> 请关闭再测试优选！(IP: \${ip})\`;
                color = "red";
            }
            notice.innerHTML = message;
            notice.style.color = color;
        } catch (e) {
            notice.textContent = "⚠️ 网络检测失败";
            notice.style.color = "orange";
        }
    }
    window.addEventListener("DOMContentLoaded", detectProxyOrVPN);
    
  `;
}