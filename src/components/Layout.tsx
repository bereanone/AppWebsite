import Header from "./Header";
import Footer from "./Footer";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="bg-parchment text-sepia font-cambria min-h-screen flex flex-col">
      <Header />

      <main className="flex-grow">
        {/* Global centering wrapper */}
        <div className="w-1/2 mx-auto px-6 py-12 bg-white">
          {children}
        </div>
      </main>

      <Footer />
    </div>
  );
}