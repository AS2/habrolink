import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
import User1 from "../components/User1";
import styles from "./SavedUsers.module.css";

const SavedUsers = () => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onInterfaceEssentialBookmarkIconClick = useCallback(() => {
    navigate("/saved-users");
  }, [navigate]);

  const onInterfaceEssentialChat1IconClick = useCallback(() => {
    navigate("/chats-page");
  }, [navigate]);

  const onInterfaceEssentialMagnifierClick = useCallback(() => {
    navigate("/search-page");
  }, [navigate]);

  const onLilProfileClick = useCallback(() => {
    navigate("/user-profile");
  }, [navigate]);

  const onSendMessageContainerClick = useCallback(() => {
    // Please sync "Message page" to the project
  }, []);

  const onInfoContainerClick = useCallback(() => {
    // Please sync "Other user1 info" to the project
  }, []);

  return (
    <div className={styles.savedUsers}>
      <Header
        bPosition="unset"
        bTop="unset"
        bLeft="unset"
        onTextClick={onTextClick}
        onInterfaceEssentialBookmarkIconClick={
          onInterfaceEssentialBookmarkIconClick
        }
        onInterfaceEssentialChat1IconClick={onInterfaceEssentialChat1IconClick}
        onInterfaceEssentialMagnifierClick={onInterfaceEssentialMagnifierClick}
        onLilProfileClick={onLilProfileClick}
      />
      <div className={styles.pageContainer}>
        <b className={styles.title}>Сохраненные пользователи</b>
        <div className={styles.searchContainer}>
          <div className={styles.foundedUsers}>
            <User1
              intersect="/intersect.svg"
              prop="Артур Шелби"
              nickname="@big_bro"
              karma="Карма: 140"
              rating="Рейтинг: 4.9"
              softKittyLovermailcom="soft_kitty_lover@mail.com"
              interfaceEssentialBookmar="/interface-essentialbookmark1.svg"
              showDot1
              showKarma
              showDot2
              showRating
              propTextTransform="capitalize"
              propColor="#000"
              propWidth="unset"
              propWidth1="unset"
              propWidth2="unset"
              propWidth3="unset"
              onSendMessageContainerClick={onSendMessageContainerClick}
              onInfoContainerClick={onInfoContainerClick}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default SavedUsers;
