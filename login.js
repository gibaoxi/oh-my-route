const axios = require('axios');
const { telegram } = require('./notify'); // 从 notify.js 导入 telegram 模块

// 登录功能
const login = async () => {
    const username = process.env.EMAIL;
    const password = process.env.B4_PASSWORD;

    if (!username || !password) {
        const errorMessage = "请设置 PARSE_USERNAME 和 PARSE_PASSWORD 环境变量";
        console.error(errorMessage);
        await telegram(errorMessage); // 发送 Telegram 通知
        process.exit(1);
    }

    const loginUrl = "https://parseapi.back4app.com/login";
    const loginHeaders = {
        "X-Parse-Application-Id": "BCrUQVkk80pCdeImSXoKXL5ZCtyyEZwbN7mAb11f",
        "X-Parse-REST-API-Key": "rWFPEbTs7UzkaVsIXnQ4qmmr9oWqwXfiiJehtIZu",
        "X-Parse-Revocable-Session": "1"
    };

    try {
        const loginResponse = await axios.post(loginUrl, null, {
            headers: loginHeaders,
            params: { username, password }
        });
        const successMessage = "登录成功！\n响应数据: " + JSON.stringify(loginResponse.data);
        console.log(successMessage);
        await telegram(successMessage); // 发送 Telegram 通知
    } catch (error) {
        let errorMessage = "登录失败！\n";
        if (error.response) {
            errorMessage += `状态码: ${error.response.status}\n错误信息: ${JSON.stringify(error.response.data)}`;
        } else {
            errorMessage += `请求错误: ${error.message}`;
        }
        console.error(errorMessage);
        await telegram(errorMessage); // 发送 Telegram 通知
    }
};

// Koyeb API 请求功能
const fetchKoyebApps = async () => {
    const api = process.env.KOYEB_API;

    if (!api) {
        const errorMessage = "请设置 KOYEB_API 环境变量";
        console.error(errorMessage);
        await telegram(errorMessage); // 发送 Telegram 通知
        process.exit(1);
    }

    const url = "https://app.koyeb.com/v1/apps";
    const apiKey = api;
    const headers = { Authorization: `Bearer ${apiKey}` };

    try {
        const response = await axios.get(url, { headers });
        const successMessage = "Koyeb 请求成功！\n响应数据: " + JSON.stringify(response.data);
        console.log(successMessage);
        await telegram(successMessage); // 发送 Telegram 通知
    } catch (error) {
        let errorMessage = "Koyeb 请求失败！\n";
        if (error.response) {
            errorMessage += `状态码: ${error.response.status}\n错误信息: ${JSON.stringify(error.response.data)}`;
        } else {
            errorMessage += `请求错误: ${error.message}`;
        }
        console.error(errorMessage);
        await telegram(errorMessage); // 发送 Telegram 通知
    }
};

// 调用登录功能和 Koyeb 函数
const main = async () => {
    console.log("开始执行登录功能...");
    await login();  // 调用登录功能

    console.log("\n开始执行 Koyeb 请求功能...");
    await fetchKoyebApps();  // 调用 Koyeb 请求功能
};

// 运行主函数
main();
