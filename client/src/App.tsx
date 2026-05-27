import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import HomePage from "./pages/HomePage";
import CreatorPage from "./pages/CreatorPage";

export default function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/creator/:id" element={<CreatorPage />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}
