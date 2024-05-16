import { useEffect } from "react";
import {
  Routes,
  Route,
  useNavigationType,
  useLocation,
} from "react-router-dom";
import Homepage from "./pages/Homepage";
import SearchPage from "./pages/SearchPage";
import SignUp from "./pages/SignUp";
import UserProfile from "./pages/UserProfile";
import UserProfileEdit from "./pages/UserProfileEdit";
import ChatsPage from "./pages/ChatsPage";
import SavedUsers from "./pages/SavedUsers";
import SignIn from "./pages/SignIn";

function App() {
  const action = useNavigationType();
  const location = useLocation();
  const pathname = location.pathname;

  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action, pathname]);

  useEffect(() => {
    let title = "";
    let metaDescription = "";

    switch (pathname) {
      case "/":
        title = "";
        metaDescription = "";
        break;
      case "/search-page":
        title = "";
        metaDescription = "";
        break;
      case "/signup":
        title = "";
        metaDescription = "";
        break;
      case "/user-profile":
        title = "";
        metaDescription = "";
        break;
      case "/user-profile-edit":
        title = "";
        metaDescription = "";
        break;
      case "/chats-page":
        title = "";
        metaDescription = "";
        break;
      case "/saved-users":
        title = "";
        metaDescription = "";
        break;
      case "/signin":
        title = "";
        metaDescription = "";
        break;
    }

    if (title) {
      document.title = title;
    }

    if (metaDescription) {
      const metaDescriptionTag = document.querySelector(
        'head > meta[name="description"]'
      );
      if (metaDescriptionTag) {
        metaDescriptionTag.content = metaDescription;
      }
    }
  }, [pathname]);

  return (
    <Routes>
      <Route path="/" element={<Homepage />} />
      <Route path="/search-page" element={<SearchPage />} />
      <Route path="/signup" element={<SignUp />} />
      <Route path="/user-profile" element={<UserProfile />} />
      <Route path="/user-profile-edit" element={<UserProfileEdit />} />
      <Route path="/chats-page" element={<ChatsPage />} />
      <Route path="/saved-users" element={<SavedUsers />} />
      <Route path="/signin" element={<SignIn />} />
    </Routes>
  );
}
export default App;
