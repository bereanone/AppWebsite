export default function Header() {
  return (
    <header className="bg-parchment text-sepia font-serif shadow">
      <div className="w-full px-6 py-3 flex justify-between items-center">
        {/* Logo + Title */}
        <div className="flex items-center space-x-3">
          <img
            src="/Logo2Small.png"
            alt="Biblical Heritage Logo"
            className="block w-[32px] h-[32px] object-contain shrink-0"
          />
          <span className="text-lg font-bold">Biblical Heritage</span>
        </div>

        {/* Navigation */}
        <nav className="space-x-6 text-sm font-semibold">
          <a href="#features" className="hover:text-verse transition">
            Features
          </a>
          <a href="#about" className="hover:text-verse transition">
            About
          </a>
          <a href="#contact" className="hover:text-verse transition">
            Contact
          </a>
          <a href="#privacy" className="hover:text-verse transition">
            Privacy
          </a>
        </nav>
      </div>
    </header>
  );
}
