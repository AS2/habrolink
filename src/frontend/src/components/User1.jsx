import { useMemo } from "react";
import styles from "./User1.module.css";

const User1 = ({
  intersect,
  prop,
  nickname,
  karma,
  rating,
  softKittyLovermailcom,
  interfaceEssentialBookmar,
  showDot1,
  showKarma,
  showDot2,
  showRating,
  propTextTransform,
  propColor,
  propWidth,
  propWidth1,
  propWidth2,
  propWidth3,
  onSendMessageContainerClick,
  onInfoContainerClick,
}) => {
  const nicknameStyle = useMemo(() => {
    return {
      textTransform: propTextTransform,
      color: propColor,
    };
  }, [propTextTransform, propColor]);

  const dot1Style = useMemo(() => {
    return {
      width: propWidth,
    };
  }, [propWidth]);

  const karmaStyle = useMemo(() => {
    return {
      width: propWidth1,
    };
  }, [propWidth1]);

  const dot2Style = useMemo(() => {
    return {
      width: propWidth2,
    };
  }, [propWidth2]);

  const ratingStyle = useMemo(() => {
    return {
      width: propWidth3,
    };
  }, [propWidth3]);

  return (
    <div className={styles.user1}>
      <div className={styles.mainInfo}>
        <img className={styles.intersectIcon} alt="" src={intersect} />
        <div className={styles.description}>
          <b className={styles.b}>{prop}</b>
          <div className={styles.habrInfo}>
            <div className={styles.nickname} style={nicknameStyle}>
              {nickname}
            </div>
            {showDot1 && (
              <div className={styles.dot1} style={dot1Style}>
                ●
              </div>
            )}
            {showKarma && (
              <div className={styles.nickname} style={karmaStyle}>
                {karma}
              </div>
            )}
            {showDot2 && (
              <div className={styles.dot2} style={dot2Style}>
                ●
              </div>
            )}
            {showRating && (
              <div className={styles.nickname} style={ratingStyle}>
                {rating}
              </div>
            )}
          </div>
          <div className={styles.softKittyLovermailcom}>
            {softKittyLovermailcom}
          </div>
        </div>
      </div>
      <div className={styles.actionsButtons}>
        <div
          className={styles.sendMessage}
          onClick={onSendMessageContainerClick}
        >
          <img
            className={styles.interfaceEssentialchat1Icon}
            alt=""
            src="/habrolinker-icon-chat.svg"
          />
        </div>
        <div className={styles.mark}>
          <img
            className={styles.interfaceEssentialchat1Icon}
            alt=""
            src={interfaceEssentialBookmar}
          />
        </div>
        <div className={styles.sendMessage} onClick={onInfoContainerClick}>
          <img
            className={styles.interfaceEssentialchat1Icon}
            alt=""
            src="/interface-essentialinformationcircle.svg"
          />
        </div>
      </div>
    </div>
  );
};

export default User1;
