export default function Footer() {
  return (
    <footer className="bg-[#1a0e0e] text-[#fdf6e3] text-center py-6 mt-12 border-t border-[#fdf6e3]/20">
      <div className="flex justify-center items-center space-x-2">
        <img
          src="/Logo2Small.png"
          alt="Biblical Heritage Logo"
          className="h-4 w-auto object-contain align-middle"
        />
        <span className="text-sm">
          © 2025 Biblical Heritage. All rights reserved.
        </span>
      </div>
    </footer>
  );
}
