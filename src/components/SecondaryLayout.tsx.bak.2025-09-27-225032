import Header from "./Header";
import Footer from "./Footer";

export default function SecondaryLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="bg-white text-sepia font-cambria min-h-screen flex flex-col">
      {/* Header */}
      <Header />

      {/* Main content */}
      <main className="flex-grow max-w-4xl mx-auto px-6 py-16">
        {children}
      </main>

      {/* Footer */}
      <Footer />
    </div>
  );
}