const axios = require('axios');

// Server酱 通知
const serverchan = async (title, message) => {
    /**
     * 使用 Server酱 发送通知
     * @param {string} title - 通知标题
     * @param {string} message - 通知内容
     */
    const sendkey = process.env.SENDKEY; // 从环境变量获取 SendKey
    if (!sendkey) {
        throw new Error("请设置环境变量 SENDKEY");
    }

    const url = `https://sctapi.ftqq.com/${sendkey}.send`;
    const data = {
        title: title,
        desp: message
    };

    try {
        const response = await axios.post(url, data);
        if (response.status === 200) {
            console.log("Server酱 通知已发送！");
        } else {
            console.log(`Server酱 通知发送失败: ${response.data}`);
        }
    } catch (error) {
        console.error(`Server酱 通知发送失败: ${error.message}`);
    }
};

// PushPlus 通知
const pushplus = async (title, message) => {
    /**
     * 使用 PushPlus 发送通知
     * @param {string} title - 通知标题
     * @param {string} message - 通知内容
     */
    const token = process.env.PUSHPLUS_TOKEN; // 从环境变量获取 Token
    if (!token) {
        throw new Error("请设置环境变量 PUSHPLUS_TOKEN");
    }

    const url = 'http://www.pushplus.plus/send';
    const data = {
        token: token,
        title: title,
        content: message
    };

    try {
        const response = await axios.post(url, data);
        if (response.status === 200) {
            console.log("PushPlus 通知已发送！");
        } else {
            console.log(`PushPlus 通知发送失败: ${response.data}`);
        }
    } catch (error) {
        console.error(`PushPlus 通知发送失败: ${error.message}`);
    }
};

// Telegram 通知
const telegram = async (message) => {
    /**
     * 使用 Telegram 发送通知
     * @param {string} message - 通知内容
     */
    const botToken = process.env.TG_BOT_TOKEN; // 从环境变量获取 Bot Token
    const chatId = process.env.TG_USER_ID;    // 从环境变量获取 Chat ID
    if (!botToken || !chatId) {
        throw new Error("请设置环境变量 TG_BOT_TOKEN 和 TG_USER_ID");
    }

    const url = `https://api.telegram.org/bot${botToken}/sendMessage`;
    const data = {
        chat_id: chatId,
        text: message
    };

    try {
        const response = await axios.post(url, data);
        if (response.status === 200) {
            console.log("Telegram 通知已发送！");
        } else {
            console.log(`Telegram 通知发送失败: ${response.data}`);
        }
    } catch (error) {
        console.error(`Telegram 通知发送失败: ${error.message}`);
    }
};

// Qmsg 通知
const qmsg = async (message, qq = null) => {
    /**
     * 使用 Qmsg 发送通知
     * @param {string} message - 通知内容
     * @param {string} qq - 接收消息的 QQ 号（可选）
     */
    const qmsgKey = process.env.QMSG_KEY; // 从环境变量获取 Qmsg Key
    if (!qmsgKey) {
        throw new Error("请设置环境变量 QMSG_KEY");
    }

    const url = `https://qmsg.zendee.cn/send/${qmsgKey}`;
    const data = {
        msg: message
    };
    if (qq) {
        data.qq = qq;
    }

    try {
        const response = await axios.post(url, data);
        if (response.status === 200) {
            console.log("Qmsg 通知已发送！");
        } else {
            console.log(`Qmsg 通知发送失败: ${response.data}`);
        }
    } catch (error) {
        console.error(`Qmsg 通知发送失败: ${error.message}`);
    }
};

// 导出函数
module.exports = {
    serverchan,
    pushplus,
    telegram,
    qmsg
};
