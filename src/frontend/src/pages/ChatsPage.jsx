import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import StateFilled from "../components/StateFilled";
import ToggleTrueStateDefaultLa1 from "../components/ToggleTrueStateDefaultLa1";
import styles from "./ChatsPage.module.css";

const ChatsPage = () => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onInterfaceEssentialBookmarkIconClick = useCallback(() => {
    navigate("/saved-users");
  }, [navigate]);

  const onInterfaceEssentialMagnifierClick = useCallback(() => {
    navigate("/search-page");
  }, [navigate]);

  const onLilProfileClick = useCallback(() => {
    navigate("/user-profile");
  }, [navigate]);

  return (
    <div className={styles.chatsPage}>
      <HabrolinkerHeader
        bPosition="unset"
        bTop="unset"
        bLeft="unset"
        onTextClick={onTextClick}
        onInterfaceEssentialBookmarkIconClick={
          onInterfaceEssentialBookmarkIconClick
        }
        onInterfaceEssentialMagnifierClick={onInterfaceEssentialMagnifierClick}
        onLilProfileClick={onLilProfileClick}
      />
      <div className={styles.pageContainer}>
        <b className={styles.title}>Чаты</b>
        <div className={styles.chatsContainer}>
          <div className={styles.chatsList}>
            <div className={styles.user1}>
              <img
                className={styles.intersectIcon}
                alt=""
                src="/intersect3.svg"
              />
              <b className={styles.b}>Артур Шелби</b>
            </div>
            <div className={styles.user11}>
              <img
                className={styles.intersectIcon}
                alt=""
                src="/intersect4.svg"
              />
              <b className={styles.b}>Джон Шелби</b>
            </div>
            <div className={styles.user11}>
              <img
                className={styles.intersectIcon}
                alt=""
                src="/intersect5.svg"
              />
              <b className={styles.b2}>Майкл Грей (Шелби)</b>
            </div>
          </div>
          <div className={styles.currentChat}>
            <div className={styles.reciverInfo}>
              <div className={styles.description}>
                <b className={styles.b3}>Артур Шелби</b>
                <div className={styles.softKittyLovermailcom}>
                  soft_kitty_lover@mail.com
                </div>
              </div>
              <img
                className={styles.intersectIcon}
                alt=""
                src="/intersect3.svg"
              />
            </div>
            <div className={styles.messages}>
              <div className={styles.mymessages}>
                <div className={styles.msg1}>
                  <div className={styles.div}>
                    <p className={styles.p}>{`Артур, нужна твоя помощь. `}</p>
                    <p className={styles.p}>Приезжай в паб.</p>
                  </div>
                </div>
              </div>
              <div className={styles.reciverMsgs}>
                <div className={styles.msg2}>
                  <div className={styles.div}>Хорошо, Том. Скоро буду.</div>
                </div>
                <div className={styles.msg2}>
                  <div className={styles.div2}>
                    Ой, Томми, прости. Сорвался, сообщение от злости удалил.
                    Напиши еще раз, куда подъехать :*.
                  </div>
                </div>
              </div>
              <div className={styles.newmsgbox}>
                <StateFilled
                  labelText="Новое сообщение"
                  prefix="$"
                  inputText="xd"
                  eye="/eye.svg"
                  helperText="(2/1000)"
                  showHelperText
                  showPrefix={false}
                  showIcon={false}
                  stateFilledWidth="unset"
                  stateFilledBorderRadius="10px"
                  stateFilledFlex="1"
                  frameDivBackgroundColor="#f5f5f5"
                  frameDivWidth="638px"
                  helperTextWidth="unset"
                  helperTextAlignSelf="stretch"
                />
                <div className={styles.arrowsChevronchevronRightWrapper}>
                  <img
                    className={styles.arrowsChevronchevronRightIcon}
                    alt=""
                    src="/arrowschevronchevronright.svg"
                  />
                </div>
              </div>
              <ToggleTrueStateDefaultLa1
                checkBoxVariant14="/checkboxvariant14.svg"
                label="Отправить сообщение на почту"
                labelTextTransform="unset"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatsPage;
