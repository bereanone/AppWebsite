export default function Footer() {
  return (
    <footer className="footer">
      <img
        src={`${import.meta.env.BASE_URL}Small.png`}
        alt="Biblical Heritage Logo Small"
        className="logo"
      />
      <p>© 2025 Biblical Heritage. All rights reserved. | email: OurBiblicalHeritage@gmail.com</p>
    </footer>
  );
}
