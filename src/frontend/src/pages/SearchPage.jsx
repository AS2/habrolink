import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
import FiltersBlock from "../components/FiltersBlock";
import User1 from "../components/User1";
import styles from "./SearchPage.module.css";

const SearchPage = () => {
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

  const onSendMessageContainer2Click = useCallback(() => {
    // Please sync "Recived message page" to the project
  }, []);

  const onInfoContainer2Click = useCallback(() => {
    // Please sync "Other user2 info" to the project
  }, []);

  const onSendMessageContainer3Click = useCallback(() => {
    // Please sync "Recived message page" to the project
  }, []);

  const onInfoContainer3Click = useCallback(() => {
    // Please sync "Other user3 info" to the project
  }, []);

  return (
    <div className={styles.searchPage}>
      <Header
        onTextClick={onTextClick}
        onInterfaceEssentialBookmarkIconClick={
          onInterfaceEssentialBookmarkIconClick
        }
        onInterfaceEssentialChat1IconClick={onInterfaceEssentialChat1IconClick}
        onInterfaceEssentialMagnifierClick={onInterfaceEssentialMagnifierClick}
        onLilProfileClick={onLilProfileClick}
      />
      <div className={styles.pageContainer}>
        <b className={styles.title}>Поиск</b>
        <div className={styles.searchContainer}>
          <FiltersBlock />
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
              onSendMessageContainerClick={onSendMessageContainerClick}
              onInfoContainerClick={onInfoContainerClick}
            />
            <User1
              intersect="/intersect1.svg"
              prop="Джон Шелби"
              nickname="@lil_bro"
              karma="Карма: 124"
              rating="Рейтинг: 4.6"
              softKittyLovermailcom="prettygoodboi@mail.com"
              interfaceEssentialBookmar="/interface-essentialbookmark2.svg"
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
              onSendMessageContainerClick={onSendMessageContainer2Click}
              onInfoContainerClick={onInfoContainer2Click}
            />
            <User1
              intersect="/intersect2.svg"
              prop="Майкл Грей (Шелби)"
              nickname="-Не привязан аккаунт в Хабре-"
              karma="Карма: 140"
              rating="Рейтинг: 4.9"
              softKittyLovermailcom="littlebigman@mail.com"
              interfaceEssentialBookmar="/interface-essentialbookmark1.svg"
              showDot1={false}
              showKarma={false}
              showDot2={false}
              showRating={false}
              propTextTransform="unset"
              propColor="#535353"
              propWidth="15px"
              propWidth1="86px"
              propWidth2="15px"
              propWidth3="98px"
              onSendMessageContainerClick={onSendMessageContainer3Click}
              onInfoContainerClick={onInfoContainer3Click}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
