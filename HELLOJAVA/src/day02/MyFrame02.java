package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;


// MyFrame02
// JLabel -> 2 lbl
// Jbutton -> btn increase
// click event => lbl++
public class MyFrame02 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame02 frame = new MyFrame02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("0");
		lbl.setBounds(88, 113, 57, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("Click");
		btn.addMouseListener(new MouseAdapter() {
			int cnt = 0;
			@Override
			public void mouseClicked(MouseEvent e) {
				lbl.setText(String.valueOf(cnt++));
			}
		});
		btn.setBounds(171, 109, 97, 23);
		contentPane.add(btn);
	}

}
