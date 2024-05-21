import {useCallback, useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import StateFilled from "../components/StateFilled";
import ToggleTrueStateDefaultLa1 from "../components/ToggleTrueStateDefaultLa1";
import styles from "./ChatsPage.module.css";
import {SendToBackendAuthorized} from "../utils";
import HabrolinkerTextField from "../components/HabrolinkerTextField";

const ChatsPage = () => {
    const navigate = useNavigate();
    const [openedDialog, setOpenedDialog] = useState(null);
    const [dialogInfo, setDialogInfo] = useState(null);
    const [userChats, setUserChats] = useState([]);
    const [time, setTime] = useState(Date.now());
    const [currentMsg, setCurrentMsg] = useState("");


    // try to deduce currently opened dialog
    useEffect(() => {
        const queryParameters = new URLSearchParams(window.location.search)
        const chatId = queryParameters.get("chatId")

        if (chatId != undefined && chatId != "") {
            setOpenedDialog(chatId);
        }
    }, []);

    // get all chats related to current user
    useEffect(() => {
        async function fetchData() {
            let chatLists = await SendToBackendAuthorized("POST", "/message/chats", {});
            if (chatLists != null) {
                setUserChats(chatLists.chats);
            }
        }

        fetchData()
    }, [])

    // if clicked on avatar -> show requested dialog
    function onAvatar(data) {
        setOpenedDialog(data);
    }

    // on each update of openedDialog we should update messages inside it too
    useEffect(() => {
        async function fetchData() {
            let dialog = await SendToBackendAuthorized("POST", "/message/dialog", {user_id: openedDialog});
            if (dialog != null) {
                setDialogInfo(dialog);
            }
        }

        if (openedDialog != null)
            fetchData()
    }, [openedDialog]);

    function onMessage(data) {
        setCurrentMsg(data);
    }

    const onSend = useCallback(() => {
        async function fetchData() {
            await SendToBackendAuthorized("PUT", "/message/send", {
                user_id: dialogInfo.other_user_id,
                message: currentMsg
            });
            setCurrentMsg("");
        }

        fetchData()
    }, [currentMsg]);

    useEffect(() => {
        const interval = setInterval(() => {
            async function fetchData() {
                let dialog = await SendToBackendAuthorized("POST", "/message/dialog", {user_id: openedDialog});
                if (dialog != null) {
                    setDialogInfo(dialog);
                }
            }

            if (openedDialog != null)
                fetchData()
        }, 1000); //set your time here. repeat every 5 seconds

        return () => clearInterval(interval);
    }, [openedDialog]);

    return (
        <div className={styles.chatsPage}>
            <HabrolinkerHeader/>
            <div className={styles.pageContainer}>
                <b className={styles.title}>Чаты</b>
                <div className={styles.chatsContainer}>
                    <div className={styles.chatsList}>
                        {userChats.map((elem, i) => (
                            <div key={i} className={styles.chatListElement} onClick={() => onAvatar(elem.user_id)}>
                                <img
                                    className={styles.chatAvatar}
                                    alt=""
                                    src={elem.avatar}
                                />
                                <b className={styles.chatName}>{elem.name == "" ? elem.login : elem.name}</b>
                            </div>
                        ))}
                    </div>
                    {openedDialog != null && dialogInfo != null &&
                        <div className={styles.currentChat}>
                            <div className={styles.reciverInfo}>
                                <img
                                    className={styles.chatAvatar}
                                    alt=""
                                    src={dialogInfo.other_user_avatar}
                                />
                                <div className={styles.description}>
                                    <b className={styles.chatName}>{dialogInfo.other_user_name == "" ? dialogInfo.other_user_login : dialogInfo.other_user_name}</b>
                                    <div className={styles.mail}>
                                        {dialogInfo.other_user_login}
                                    </div>
                                </div>
                            </div>
                            <div className={styles.messages}>
                                {
                                    dialogInfo.messages.map((msg, i) => (
                                        msg.from_id == dialogInfo.this_user_id
                                            ?
                                            <div key={i} className={styles.mymessages}>
                                                <div className={styles.msg1}>
                                                    <div className={styles.div}>
                                                        <p className={styles.p}>{msg.message}</p>
                                                    </div>
                                                </div>
                                            </div>
                                            :
                                            <div key={i} className={styles.reciverMsgs}>
                                                <div className={styles.msg2}>
                                                    <div className={styles.div}>
                                                        <p className={styles.p}>{msg.message}</p>
                                                    </div>
                                                </div>
                                            </div>
                                    ))

                                }

                            </div>
                            <div className={styles.newmsgbox}>
                                <div style={{flexGrow:1}}>
                                <HabrolinkerTextField key={"message"} label="" placeholder="Новое сообщение"
                                                      value={currentMsg} onChangeValue={onMessage}/>
                                </div>
                                <div className={styles.arrowsChevronchevronRightWrapper} onClick={onSend}>
                                    <img
                                        className={styles.arrowsChevronchevronRightIcon}
                                        alt=""
                                        src="/arrowschevronchevronright.svg"
                                    />
                                </div>

                            </div>
                        </div>}
                </div>
            </div>
        </div>
    );
};

export default ChatsPage;
