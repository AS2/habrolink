import { useMemo } from "react";
import styles from "./Header.module.css";

const Header = ({
  bPosition,
  bTop,
  bLeft,
  onTextClick,
  onInterfaceEssentialBookmarkIconClick,
  onInterfaceEssentialChat1IconClick,
  onInterfaceEssentialMagnifierClick,
  onLilProfileClick,
}) => {
  const headerStyle = useMemo(() => {
    return {
      position: bPosition,
      top: bTop,
      left: bLeft,
    };
  }, [bPosition, bTop, bLeft]);

  return (
    <div className={styles.header} style={headerStyle}>
      <b className={styles.b} onClick={onTextClick}>
        <span>{`{`}</span>
        <span className={styles.span}>Хабро:</span>
        <span>{`Линкер}`}</span>
      </b>
      <div className={styles.headerRight}>
        <img
          className={styles.interfaceEssentialbookmarkIcon}
          alt=""
          src="/interface-essentialbookmark.svg"
          onClick={onInterfaceEssentialBookmarkIconClick}
        />
        <img
          className={styles.interfaceEssentialbookmarkIcon}
          alt=""
          src="/interface-essentialchat1.svg"
          onClick={onInterfaceEssentialChat1IconClick}
        />
        <img
          className={styles.interfaceEssentialbookmarkIcon}
          alt=""
          src="/interface-essentialmagnifier.svg"
          onClick={onInterfaceEssentialMagnifierClick}
        />
        <img
          className={styles.interfaceEssentialbellIcon}
          alt=""
          src="/interface-essentialbell@2x.png"
        />
        <img
          className={styles.lilProfileIcon}
          alt=""
          src="/lil-profile.svg"
          onClick={onLilProfileClick}
        />
      </div>
    </div>
  );
};

export default Header;
