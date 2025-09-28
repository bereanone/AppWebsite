import Hero from "./components/Hero";
import Features from "./components/Features";
import About from "./components/About";
import Privacy from "./components/Privacy";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div className="min-h-screen bg-[#1a0e0e] text-[#fdf6e3] flex justify-center">
      <main className="w-full max-w-6xl px-6 py-12">
        <Hero />
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 mt-12 text-left">
          <div className="space-y-12">
            <Features />
            <About />
          </div>
          <div className="space-y-12">
            <Privacy />
            <Contact />
          </div>
        </div>
        <Footer />
      </main>
    </div>
  );
}
