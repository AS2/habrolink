import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
import UserInfo1 from "../components/UserInfo1";
import styles from "./UserProfileEdit.module.css";

const UserProfileEdit = () => {
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

  return (
    <div className={styles.userProfileEdit}>
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
      <UserInfo1 />
    </div>
  );
};

export default UserProfileEdit;
